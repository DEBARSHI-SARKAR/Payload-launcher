import socket

def payload(ip, port, file):
    with socket.create_connection((ip, port), timeout=3) as sock:
        with open(file, "rb") as f:
            while chunk := f.read(4096):
                if not chunk:
                    break
                sock.sendall(chunk)
