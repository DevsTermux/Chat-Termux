import socket
#import sys

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ipaddr = input("IP: ")
port = input("PORT: ")
user = input("Usuario: ")
cli_sock.connect((IP_Address, Port))

while True:
	data = input('> ')
	print ('data= ', data)
	if not data:
		break
	cli_sock.send(data)
	data = cli_sock.recv(2048)
	if not data:
		break
	print (data)

cli_sock.close()
