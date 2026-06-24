import socket
from concurrent.futures import ThreadPoolExecutor

def scan_single_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            s.close()

            return {
                "port": port,
                "service": service
            }

        s.close()

    except:
        pass

    return None


def scan_ports(target, start_port, end_port):

    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:

        results = executor.map(
            lambda port: scan_single_port(target, port),
            range(start_port, end_port + 1)
        )

        for result in results:
            if result:
                open_ports.append(result)

    open_ports.sort(key=lambda x: x["port"])

    return open_ports