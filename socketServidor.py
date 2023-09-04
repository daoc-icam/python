import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8080))
servidor.listen()

while True:
    cliente, address = servidor.accept()
    while True:
        data = cliente.recv(256)
        if not data:
            cliente.close()
            break
        cliente.sendall(data.upper())