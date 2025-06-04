import socket
import threading

def scan_port(ip, port, verbose=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    if result == 0:
        return port, True
    else:
        if verbose:
            print(f'{ip}:{port} - FermÃ©')
        return port, False

def scan_ports(ip, ports, verbose=False):
    results = {}
    threads = []

    def worker(p):
        port, is_open = scan_port(ip, p, verbose)
        results[port] = is_open

    for port in ports:
        t = threading.Thread(target=worker, args=(port,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    open_ports = [port for port, open in results.items() if open]
    closed_ports = [port for port, open in results.items() if not open]
    return open_ports, closed_ports