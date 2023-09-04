import socket

cliente = socket.socket()
cliente.connect(('localhost', 8080))

while True:
    data = input('Ingrese dato: ')
    cliente.sendall(str.encode(data))
    print(bytes.decode(cliente.recv(256)))