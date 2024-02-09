import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_address = ("192.168.111.69", 7777)
my_socket.bind(my_address)

my_socket.listen()

f = open("site.html", encoding="utf8")
content = f.read()
f.close()



while True:
    client, address = my_socket.accept()

    data = client.recv(1024)
    request = data.decode("utf8")
    print(f"написали те от {address}: \n{request}")


    http_head = f"""HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(content)} 
"""

    response = http_head + content
    client.send(response.encode("utf8"))

    client.close()