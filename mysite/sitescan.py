import nmap
import sqlite3

def scan_hosts(targets):
    nm = nmap.PortScanner()
    nm.scan(hosts=targets)
    host_list = [(x, nm[x]['hostnames'][0]['name'], str(list(nm[x]['tcp'].keys()))) for x in nm.all_hosts()]
    print(host_list)
    conn = sqlite3.connect('site.sqlite')
    conn.executemany('INSERT INTO clients values (?,?,?)',host_list)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    scan_hosts('127.0.0.1')
