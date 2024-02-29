import socket
import json

class AbcClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.adress = self.host, self.port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def send(self, word: str):
        data = {'word': word}
        msg = json.dumps(data)
        self.sock.sendto(msg.encode('utf8'), (self.adress))

    def connect(self):
        self.send('hello')

    def end(self):
        data = {'gameover': ''}
        msg = json.dumps(data)
        self.sock.sendto(msg.encode('utf8'), (self.adress))

    def _receive(self):
        data, self.remote = self.sock.recvfrom(1024)
        return data.decode('utf8')
        
    def receive(self):
        msg = self._receive()
        data = json.loads(msg)
        if 'word' in data:
            return data['word']
        elif 'gameover' in data:
            return ''
        elif 'hello' in data:
            return 'hello'
        else:
            print('AbcClient:: Bad data received')