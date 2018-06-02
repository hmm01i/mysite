import sqlite3
import config

db = config.database
def init_db():
    cn = sqlite3.connect(db)
    with cn:
        cr = cn.cursor()
        cr.execute('CREATE TABLE IF NOT EXISTS clients (ip TEXT, hostname TEXT)')
    cn.close()
    print('initialized db')

if __name__ == "__main__":
    init_db()
