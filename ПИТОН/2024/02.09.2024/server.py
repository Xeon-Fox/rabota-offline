import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_address = ("192.168.111.69", 7777)

my_socket.bind(my_address)

running = True
while running:
    data, address = my_socket.recvfrom(2048)
    message = data.decode("utf8")
    print(f"bip bop: {message} from {address}")
    if message == "exit":
        running = False