'''
Job to scan network and store list of members in database
'''
import sys
import datetime
import nmap
from sqlalchemy import create_engine
from mysite import db
import mysite
from mysite.models import Host, Subnet

def scan(scanrange):
    '''
    do a simple scan and return results
    '''
    print(scanrange)
    scanner = nmap.PortScanner()
    scanner.scan(hosts=scanrange, arguments='-sP')
    host_list = [(x, scanner[x]['hostnames'][0]['name']) for x in scanner.all_hosts()]
    return host_list


def update_db(host_list):
    '''
    update db using builtin sqlite
    '''
    conn = mysite.database.connect_db()
    with conn:
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS clients')
        conn.commit()
        cur.execute('CREATE TABLE clients (ip text, hostname text)')
        for host in host_list:
            conn.execute("INSERT INTO clients VALUES(?,?)", (host))


def update_hosts(host_list):
    '''
    update db using sqlalchemy
    '''
    for host in host_list:
        print(host[0], host[1])
        hostentry = Subnet.query.filter_by(ip=host[0]).first()
        if hostentry != None:
            hostentry.hostname = host[1]
            hostentry.last_updated = datetime.datetime.now()
            db.session.flush()
        else:
            db.session.add(Subnet(ip=host[0],
                                  hostname=host[1],
                                  last_updated=datetime.datetime.now()))
    db.session.commit()


def run_job(scanrange='127.0.0.1'):
    '''
    The job that strings funcs together
    '''
    update_hosts(scan(scanrange))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sitescan(sys.argv[1]))
    else:
        print(sitescan('192.168.1.0/24'))
