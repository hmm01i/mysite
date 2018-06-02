import nmap
import sqlite3
import config
import database

def scan_hosts(targets):
    nm = nmap.PortScanner()
    nm.scan(hosts=targets,arguments='-sP')
    host_list = [(x, nm[x]['hostnames'][0]['name']) for x in nm.all_hosts()]
    return host_list


def update_clients(host_list):
    conn = database.connect_db()
    with conn:
        cr = conn.cursor()
        cr.execute('DROP TABLE IF EXISTS clients')
        conn.commit()
        cr.execute('CREATE TABLE clients (ip text, hostname text)')
        for h in host_list:
            conn.execute("INSERT INTO clients VALUES(?,?)",(h))

if __name__ == "__main__":
    hosts = scan_hosts('192.168.1.0/24')
    update_clients(hosts)
