import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
	print ("Modo correto de usar: script, IP Address, port number")
	exit()
IP_Address = str(sys.argv[1])
Port = int(sys.argv[2])
user = input("Seu nome: ")
server.connect((IP_Address, Port))

while True:
	sockets_list = [sys.stdin, server]
	read_sockets, write_sockets, error_sockets = select.select(sockets_list, [], [])
	for socks in read_sockets:
		if socks == server:
			message = socks.recv(2048)
			print (message)
		else:
			message = sys.stdin.readline()
			server.send(user + message)
			sys.stdout.write("<"+user+">")
			sys.stdout.write(message)
			sys.stdout.flush()

server.close()
