import sqlite3
from functools import reduce

def _init_counters(con):
    cur = con.cursor()
    cur.execute('''create table counters (namespace text unique not null primary key, last_value integer)''')

def _create_counter(con, namespace):
    cur = con.cursor()
    cur.execute('''insert into counters values (?, 0)''', (namespace,))

def counter_next(cur, namespace):
    cur.execute('''UPDATE counters SET last_value = (SELECT last_value FROM counters WHERE namespace == ?) + 1 WHERE namespace == ?''', (namespace, namespace))
    return list(cur.execute('''SELECT last_value FROM counters WHERE namespace == ?''', (namespace, )))[0][0]

def _init_relations(con):
    cur = con.cursor()
    # Create table
    cur.execute('''CREATE TABLE data
            (entity integer not null,
            attribute text not null,
            value text,
            trans integer not null,
            operation integer not null,
            unique(entity, attribute, trans)
            check((operation != 0 and value is not null) or (operation == 0 and value is null)))''')
    # Create indexes
    cur.execute('''create index eavt on data (entity, attribute, value, trans)''')
    cur.execute('''create index aevt on data (attribute, entity, value, trans)''')
    cur.execute('''create index avet on data (attribute, value, entity, trans)''')
    cur.execute('''create index vaet on data (value, attribute, entity, trans)''')

def _create_counters(con):
    _create_counter(con, "entity")
    _create_counter(con, "transaction")

def setup_database(con):
    _init_relations(con)
    _init_counters(con)
    _create_counters(con)

def _arg_quote(arg):
    if arg is None:
        return "NULL"
    elif isinstance(arg, int):
        return str(arg)
    elif isinstance(arg, str):
        return '"' + arg + '"'
    else:
        raise TypeError("Must be int or str not " + str(type(arg)))

def _hydrate(query_args):
    query, args = query_args
    new_args = tuple(map(_arg_quote, args))
    new_query = query.replace("?", "%s")
    return new_query % new_args

def _to_subquery(query_args):
    (query, args) = query_args
    return ("(" + query + ")", args)

def _to_compound_query(*queries):
    full_query = reduce(lambda x,y: x + " " + y, [query[0] for query in queries])
    full_args = reduce(lambda x,y: x+y, [query[1] for query in queries])
    return (full_query, full_args)

def query_insert_attribute(entity, attribute, value, transaction_id):
    query = """insert or ignore into data values (?, ?, ?, ?, ?)"""
    args = (entity, attribute, value, transaction_id, 1)
    return (query, args)

def query_all_attribute_newest_version(attribute):
    query = '''select value from (select value, operation from data where attribute == ? group by entity, attribute having max(trans)) where operation == 1'''
    args = (attribute, )
    return (query, args)

def query_all_entities_with_attributes(*attributes, **kwargs):
    constraint = kwargs.get("constraint")
    query = ("SELECT", tuple())
    sep = ""
    for attribute in attributes:
        name = attribute.replace("/", "_")
        attr_extract = """%sMAX(CASE WHEN (attribute = "%s") THEN value ELSE null END) AS %s""" % (sep, attribute, name)
        query = _to_compound_query(query, (attr_extract, tuple()))
        sep = ", "
    query = _to_compound_query(query, ("FROM data", tuple()))
    if constraint:
        query = _to_compound_query(query, ("where", tuple()) )
        query = _to_compound_query(query, constraint)
    query = _to_compound_query(query, ('''GROUP BY entity ORDER BY entity''', tuple()))
    print(query)
    return query

def query_attribute_newest_version(entity, attribute):
    query = '''select value from (select value, operation from data where entity == ? and attribute == ? group by attribute having max(trans)) where operation == 1'''
    args = (entity, attribute)
    return (query, args)

def query_entity_newest_version(entity):
    query = '''select attribute, value from (select attribute, value, operation from data where entity == ? group by attribute having max(trans)) where operation == 1'''
    args = (entity, )
    return (query, args)

def query_newest_version_value_match(entity, attribute, value):
    prefix = ("select * from", tuple())
    newest_version = _to_subquery(query_attribute_newest_version(entity, attribute))
    match_check = ("where value == ?", (value, ))
    return _to_compound_query(prefix, newest_version, match_check)

    query = """select * from data where
    entity == ? and
    attribute == ? and
    operation == 1
    order by trans desc limit 1"""
    args = (entity, attribute, value)
    return (query, args)

def query_upsert_attribute(transaction_id, entity, kv):
    insert = ("""INSERT OR IGNORE INTO data""", tuple())
    full_query = [insert]
    for i, (attribute, value) in enumerate(kv.items()):
        operation = 0 if value is None else 1
        select = ("""SELECT ?, ?, ?, ?, ? WHERE NOT EXISTS""",
                (entity, attribute, value, transaction_id, operation))
        query_prior = _to_subquery(query_newest_version_value_match(entity, attribute, value))
        if i > 0:
            full_query.append( ("UNION", tuple()) )
        full_query.append(select)
        full_query.append(query_prior)
    return _to_compound_query(*full_query)

def query_insert(entity, attribute, transaction_id, operation):
    query = "insert or ignore into data values (?, ?, ?, ?, ?)"
    args = (entity, attribute, transaction_id, operation)
    return (query, args)

def transaction(con):
    cur = con.cursor()
    transaction_id = counter_next(cur, "transaction")
    def inserter(entity, kv):
        cur.execute(*query_upsert_attribute(transaction_id, entity, kv))
    inserter("transaction", {"transaction": transaction_id})
    return inserter

