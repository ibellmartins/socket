#!/usr/bin/python           # This is client.py file
# Import socket module
import socket
# Create a socket object
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Endpoint
host = '192.168.0.118'	    # IP Server
port = 10420                # Reserve a port for your service.
dest = (host,port)
s.connect(dest)

while True: 
    cli_msg = input("Cliente: ")
    if cli_msg.lower() == "quit":
        print('comando quit recebido - conexao encerrada')
        s.send(cli_msg.encode())
        break 

    s.send(cli_msg.encode())

    server_msg = s.recv(1024).decode()
    if server_msg.lower() == 'quit':
        print('comando quit recebido - conexao encerrada')
        break

    print('Servidor: ' + server_msg)

s.close()   # close the socket when done