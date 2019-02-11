import socket
import sys
from time import ctime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
	print ("Modo correto de usar: script, IP Address, port number")
	exit()
IP_Address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_Address, Port))
server.listen(50)
list_of_client = []

while True:
	print ("Aguardando conecção...")
	cli_sock, addr = server.accept()
	print ("Conectado de: ", addr[0])
	while  True:
		data = cli_sock.recv(2048)
		if not data:
			break
		cli_sock.send(('[%s] %s' %(ctime(), data)))
	cli_sock.close()
server.close()
