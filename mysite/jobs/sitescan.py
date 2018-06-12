'''
Job to scan network and store list of members in database
'''
import sys
import time
import datetime
import nmap
from mysite import db
import mysite
from mysite.models import Host, Subnet
from sqlalchemy import create_engine

def scan(scanrange):
    '''
    do a simple scan and return results
    '''
    pt = scanrange
    print(pt)
    nm = nmap.PortScanner()
    nm.scan(hosts=pt,arguments='-sP')
    host_list = [(x, nm[x]['hostnames'][0]['name']) for x in nm.all_hosts()]
    return host_list


def update_db(host_list):
    '''
    update db using builtin sqlite
    '''
    conn = mysite.database.connect_db()
    with conn:
        cr = conn.cursor()
        cr.execute('DROP TABLE IF EXISTS clients')
        conn.commit()
        cr.execute('CREATE TABLE clients (ip text, hostname text)')
        for h in host_list:
            conn.execute("INSERT INTO clients VALUES(?,?)", (h))


def update_hosts(host_list):
    '''
    update db using sqlalchemy
    '''
    for h in host_list:
        print(h[0], h[1])
        hostentry = Subnet.query(ip=h[0]).first()
        db.session.add(Subnet(ip=h[0], hostname=h[1], last_updated=datetime.datetime.now()))
    db.session.commit()


def sitescan_job(scanrange='127.0.0.1'):
    '''
    The job that strings funcs together
    '''
    update_hosts(scan(scanrange))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sitescan_job(sys.argv[1]))
    else:
        print(sitescan_job('192.168.1.0/24'))
