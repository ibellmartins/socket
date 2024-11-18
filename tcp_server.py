import socket  # Import socket module

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.0.118'  # IP address as a string
port = 10421            # Port number must be an integer
dest = (host, port)

s.bind(dest)  # Bind the socket to the host and port

s.listen(1)  # Now wait for client connection.
print("Server listening on", host, ":", port)

c, addr = s.accept()  # Establish connection with client.
print('Got connection from', addr)  # In Python 3, use print() with parentheses
# c.send('Thank you for connecting'.encode())  # Send message as bytes

while True:    
    cli_msg = c.recv(1024).decode()
    
    if cli_msg.lower() == 'quit':
        print('comando quit recebido - conexao encerrada')
        break
    print('Cliente: ', cli_msg)

    #reply to client
    server_msg = input("Servidor: ")

    if server_msg == 'quit':
        print('comando quit recebido - conexao encerrada')
        c.send(server_msg.encode())
        break

    c.send(server_msg.encode())

    
c.close()   #Close the connection after the communication
s.close()
