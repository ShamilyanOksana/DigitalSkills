import Network
import json

net = Network.Network()

data = {'file_name': 'test.txt',
        'data': "texttextetxtetxt\ntexttexttext",
        'author': '0x280c28e82f000827c8a259ba2a57bd66e89fc54c',
        'type': 'Печатные издание',
        'category': '3',
        'timeout': '0'}
data = json.dumps(data).encode()
net.send_message(data)