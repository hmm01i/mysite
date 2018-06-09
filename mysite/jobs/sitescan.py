'''
Job to scan network and store list of members in database
'''
import sys
import nmap
from mysite import db
import mysite
from mysite.models import Host

class SiteScan:
    '''
    Job to scan site.
    '''
    def __init__(self, site_range='127.0.0.1'):
        self.range = site_range

    def scan(self):
        pt = self.range
        print(pt)
        nm = nmap.PortScanner()
        nm.scan(hosts=pt,arguments='-sP')
        host_list = [(x, nm[x]['hostnames'][0]['name']) for x in nm.all_hosts()]
        return host_list


    def update_db(self, host_list):
        conn = mysite.database.connect_db()
        with conn:
            cr = conn.cursor()
            cr.execute('DROP TABLE IF EXISTS clients')
            conn.commit()
            cr.execute('CREATE TABLE clients (ip text, hostname text)')
            for h in host_list:
                conn.execute("INSERT INTO clients VALUES(?,?)",(h))


    def update_hosts(self, host_list):
        for h in host_list:
            print(h[0], h[1])
            db.session.add(Host(ip=h[0], hostname=h[1]))
        db.session.commit()


    def job(self):
        '''
        The job that strings methods together
        '''
        self.update_hosts(self.scan())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ss = SiteScan(sys.argv[1])
    else:
        ss = SiteScan()
    print(ss.job())
