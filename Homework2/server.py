import socket

host = '127.0.0.1'
port = 55555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

print("Waiting for connection ...")

client_socket, client_address = server_socket.accept()

while True:
    operation = client_socket.recv(1024).decode()
    num1 = float(client_socket.recv(1024).decode())
    num2 = float(client_socket.recv(1024).decode())

    result = None

    if operation == '1':
        result = num1 + num2
    elif operation == '2':
        result = num1 - num2
    elif operation == '3':
        result = num1 / num2
    elif operation == '4':
        result = num1 * num2

    client_socket.send(str(result).encode())

    if operation == 'q':
        client_socket.close()
        break

server_socket.close()
