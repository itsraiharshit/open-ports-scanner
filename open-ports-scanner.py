import socket
import concurrent.futures

art = '''

   ___                         ____            _            ____                                  
  / _ \ _ __   ___ _ __       |  _ \ ___  _ __| |_ ___     / ___|  ___ __ _ _ __  _ __   ___ _ __ 
 | | | | '_ \ / _ \ '_ \ _____| |_) / _ \| '__| __/ __|____\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |_| | |_) |  __/ | | |_____|  __/ (_) | |  | |_\__ \_____|__) | (_| (_| | | | | | | |  __/ |   
  \___/| .__/ \___|_| |_|     |_|   \___/|_|   \__|___/    |____/ \___\__,_|_| |_|_| |_|\___|_|   
       |_|                                                                                        

'''
print(art)
print("Type 'exit' and press 'Enter' to exit")
def get_port_name(port):
    try:
        return socket.getservbyport(port)
    except socket.error:
        return 'unknown'

def scan_port(ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    result = sock.connect_ex((ip_address, port))
    sock.close()
    if result == 0:
        return (port, get_port_name(port))
    return None

def scan_ports(hostname):
    ip_address = socket.gethostbyname(hostname)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        open_ports = [port for port in executor.map(scan_port, [ip_address]*50, [20, 21, 22, 23, 25, 53, 80, 110, 137, 139, 443, 445, 1433, 1434, 3306, 3389, 5900, 8080, 8443] + list(range(49152, 49200))) if port]
    for port in open_ports:
        print(f"Port {port[0]} is open: {port[1]}")

while True:
    hostname = input("Enter the hostname to scan: ")
    if (hostname=='exit'):
        break
    else:
        scan_ports(hostname)

