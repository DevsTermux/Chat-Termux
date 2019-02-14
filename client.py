import socket
import threading
import select
import sys

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cli_sock:
	if len(sys.argv) != 3:
		print ("Modo correto de usar: script, IP Address, port number")
		exit()
	IP_Address = str(sys.argv[1])
	Port = int(sys.argv[2])
	user = input("Seu nome: ")
	cli_sock.connect((IP_Address, Port))
#	messagem()

#def messagem():
	while True:
		whois = [sys.stdin, cli_sock] #whois registra cli_sock como entradas usando sys.stdin
		read, write, error = select.select(whois, [], []) #Seleciona whois, leia-se ele
		for i in read:
			if i is cli_sock: #Se for recebido uma resposta
				answer = cli_sock.recv(1024) #Recebi answer codificada
				if not answer:
					print ("Sem resposta \'answer\'")
					sys.exit()
				print ('\n{}'.format(answer.decode())) #Imprimi answer decodificada string-bytes
			else: 
				message = input('\n'"<" + user + ">: ")
				#sys.stdout.write("<" + user + ">: ")
				#message = sys.stdin.readline() #Messagem para ser enviada
				if not message: break
				cli_sock.send('{}: {}'.format(user, message).encode()) #Envia message codificada bytes-string
				sys.stdout.flush()
		#print (mes_send.recv(1024).decode())
		

#while True:
	#data = input('> ')
	#print ('data= ', data)
	#if not data:
	#	break
	#cli_sock.sendall(data.encode('utf-8'))
	#data = cli_sock.recv(1024)
	#if not data:
	#	break
	#print (message(cli_sock))
	#print (bytes(ctime(), 'utf-8'), " ", data.decode('utf-8'))

cli_sock.close()

