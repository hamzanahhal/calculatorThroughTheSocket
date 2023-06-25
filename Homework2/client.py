import socket

host = '127.0.0.1'
port = 55555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

print("Operations:")
print("1. Add two numbers")
print("2. Subtract two numbers")
print("3. Divide two numbers")
print("4. Multiply two numbers")

while True:
    operation = input("Enter the operation number (1-4), or 'q' to quit: ")
    client_socket.send(operation.encode())

    if operation == 'q':
        break

    num1 = input("Enter the first number: ")
    client_socket.send(num1.encode())

    num2 = input("Enter the second number: ")
    client_socket.send(num2.encode())

    result = client_socket.recv(1024).decode()
    print("Result:", result)

client_socket.close()
