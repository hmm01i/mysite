import sqlite3
from mysite import db

def create_tables():
    # Create table for each model if it does not exist.
    # Use the underlying peewee database object instead of the
    # flask-peewee database wrapper:
    db.create_all()

def tables(table=None):
    tables = { 'hosts': [
                ('ip', 'TEXT'),
                ('hostname', 'TEXT')
                ]
            }
    if table == None:
        return tables.keys()
    elif table in tables.keys():
        return tables[table]
    else:
        return 'table not found'

def init_table(connection, table):
    '''drops and recreates table'''
    t = tables(table)
    columns = ', '.join(['{} {}'.format(c[0],c[1]) for c in t])
    drop = 'DROP TABLE IF EXISTS {}'.format(table)
    create = 'CREATE TABLE {} ({})'.format(table,columns)
    print(drop)
    print(create)

    with connection:
        cr = connection.cursor()
        cr.execute(drop)
        connection.commit()
        cr.execute(create)
        connection.commit()
    connection.close()

def init_db(connection):
    for t in tables():
        init_table(connection,t)
    print('initialized db')

def connect_db(db=None):
    if db == None:
        db = ':memory:'
    try:
        return sqlite3.connect(db)
    except:
        return 'Could not connect to db'

if __name__ == "__main__":
    init_db(connect_db())
