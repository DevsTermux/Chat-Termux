import socket
#import sys
#from time import ctime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ipaddr = input("IP: ")
port = input("PORT: ")
server.bind((IP_Address, Port))
server.listen(50)

while True:
	print ("Aguardando conecção...")
	cli_sock, addr = server.accept()
	print ("Conectado de: ", addr)
	while  True:
		data = cli_sock.recv(2048)
		if not data:
			break
		cli_sock.send(data)
	cli_sock.close()
server.close()
