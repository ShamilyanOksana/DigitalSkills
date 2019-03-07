import socket
import json

class Network:

    def get_message(self):
        while True:
            sock = socket.socket()
            sock.bind(('', 9090))
            sock.listen(1)
            con, addr = sock.accept()
            data = con.recv(2048)
            if data:
                data = json.loads(data.decode())
                return data

    def send_message(self, data):
        data = json.dumps(data).encode()
        sock = socket.socket()
        hostname = socket.gethostname()
        my_ip = socket.gethostbyname(hostname)
        sock.connect(("192.168.1.21", 9090))
        sock.send(data)
        sock.close()

