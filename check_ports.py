import socket
import time

def check_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  # Set a timeout for the connection attempt
            s.connect((host, port))
            return True
    except (ConnectionRefusedError, socket.timeout):
        return False

def check_ports_periodically(host, ports, interval=60):
    while True:
        print(f"Checking ports on {host}...")
        for port in ports:
            if check_port(host, port):
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
        print(f"Waiting for {interval} seconds...")
        time.sleep(interval)

if __name__ == "__main__":
    host = "192.168.31.1"  # This will be the IP address for the blue team Change this before runing
    ports = [80, 443, 22, 3306]  # This will be the list of ports that you want to check

    check_ports_periodically(host, ports)
