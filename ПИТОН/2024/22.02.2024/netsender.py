import socket

class Sender:
    port = 11488
    sock = None

    def __init__(self) -> None:
        self.port = property
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, message, dest_ip):
        data = message.encode("utf8")
        addr = (dest_ip, self.port)
        self.sock.sendto(data, addr)