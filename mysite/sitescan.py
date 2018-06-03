import nmap
import sqlite3
import config
import database

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
    ss = SiteScan('192.168.1.0/28')
    print(ss.scan())
