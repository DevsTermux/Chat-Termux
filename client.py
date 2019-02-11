import socket
import sys

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Modo correto de usar: script, IP Address, port number")
	exit()
IP_Address = str(sys.argv[1])
Port = int(sys.argv[2])
user = input("Seu nome: ")
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
