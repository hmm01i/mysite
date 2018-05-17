import sqlite3

def init_db():
    cn = sqlite3.connect('site.sqlite')
    cr = cn.cursor()
    cr.execute('CREATE TABLE IF NOT EXISTS clients (ip text, hostname text, tcp text)')
    cn.commit()
    cn.close()

if __name__ == "__main__":
    init_db()
