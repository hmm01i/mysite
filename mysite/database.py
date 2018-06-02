import sqlite3
import config

db = config.database
def init_db():
    cn = sqlite3.connect(db)
    with cn:
        cr = cn.cursor()
        cr.execute('CREATE TABLE IF NOT EXISTS clients (ip text, hostname text)')
    cn.close()
    print('initialized db')

def connect_db():
    return sqlite3.connect(db)

def insert(table,record):
    conn = sqlite3.connect(db)
    with conn:
        conn.execute("INSERT INTO ? values (','.join(['?']*len(record),)",(table,*record))

def update(table,record):
    pass

def get_record(table,query):
    pass

def remove(table,record):
    pass

if __name__ == "__main__":
    init_db()
