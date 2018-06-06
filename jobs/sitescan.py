import nmap
import sqlite3
import mysite.database
import mysite
import sys

class SiteScan:
    def __init__(self,site_range='127.0.0.1'):
        self.site_range = site_range

    def scan(self):
        t = self.site_range
        nm = nmap.PortScanner()
        nm.scan(hosts=t,arguments='-sP')
        host_list = [(x, nm[x]['hostnames'][0]['name']) for x in nm.all_hosts()]
        return host_list

    def update_db(self,host_list):
        conn = database.connect_db()
        with conn:
            cr = conn.cursor()
            cr.execute('DROP TABLE IF EXISTS clients')
            conn.commit()
            cr.execute('CREATE TABLE clients (ip text, hostname text)')
            for h in host_list:
                conn.execute("INSERT INTO clients VALUES(?,?)",(h))

    def job(self):
        self.update_db(self.scan())

if __name__ == "__main__":
    if sys.argv[0]:
        ss = SiteScan(sys.argv[0])
    else:
        ss = SiteScan('127.0.0.1')
    print(ss.scan())
