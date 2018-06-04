import sqlite3
from mysite import config

db = config.database
def init_db():
    cn = connect_db()
    with cn:
        cr = cn.cursor()
        cr.execute('CREATE TABLE IF NOT EXISTS clients (ip TEXT, hostname TEXT)')
    cn.close()
    print('initialized db')

def connect_db():
    return sqlite3.connect(db)

if __name__ == "__main__":
    init_db()
