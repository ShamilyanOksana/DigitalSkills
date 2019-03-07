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
                file_name = data.get('file_name')
                file_data = data.get('data')
                with open('C:\\Users\\user\\Desktop\\Library\\not crypto\\' + file_name, 'w') as new_file:
                    new_file.write(file_data)
                return data

    def send_message(self, data):
        sock = socket.socket()
        hostname = socket.gethostname()
        my_ip = socket.gethostbyname(hostname)
        sock.connect((my_ip, 9090))
        sock.send(data)
        sock.close()

