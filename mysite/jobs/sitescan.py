'''
Job to scan network and store list of members in database
'''
import sys
import datetime
import nmap
from mysite import db
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
