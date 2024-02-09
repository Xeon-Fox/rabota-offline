import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = ("192.168.110.190", 8000)

message = "КАНЬЕ ВЕСТ ПРЕЗИДЕНТ МИРА"
data = message.encode("utf8")
my_socket.sendto(data, server)