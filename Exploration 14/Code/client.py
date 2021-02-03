import socket

HEADER = 64
PORT = 3000
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
DISCONNECT_MESSAGE = "DISCONNECT---"
ADDR = (SERVER, PORT)

client = socket.socket()
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)

def leave():
    send(DISCONNECT_MESSAGE)

while True:
    f = input('Do you want to connect? ')
    if f.lower() == 'n':
        leave()
        break
    msg = input('Message: ')
    send(msg)
    print('Message Sent')
