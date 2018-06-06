import nmap
import database
import mysite
import sys

class SiteScan:
    def __init__(self,site_range='127.0.0.1'):
        self.range = site_range

    def scan(self):
        pt = self.range
        print(pt)
        nm = nmap.PortScanner()
        nm.scan(hosts=pt,arguments='-sP')
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
    if len(sys.argv) > 1:
        ss = SiteScan(sys.argv[1])
    else:
        ss = SiteScan()
    print(ss.scan())
