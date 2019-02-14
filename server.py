import socket
import sys
import threading
#from time import ctime

#server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


#list_of_client = []

def messagem(cli_sock):
	while True:
		message = cli_sock.recv(1024)
		if not message:
			list_client.remove(cli_sock)
			break
		for msg_all in list_client: #Enviar mensagem para todos os clientes, exceto quem enviou
			if msg_all is not cli_sock:
				msg_all.send('{}'.format(message.decode()).encode('utf-8'))#{}:cli_sock.getpeername(),
		#message = input("msg: ")
		#cli_sock.sendall('(isto veio do sevidor)...a sua mensagem foi: {}\n'.format(message).encode('utf-8'))
#cli_sock, cli_addr = server.accept()
list_client = set() #Armazena conexões aqui

with socket.socket() as server:
	socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	if len(sys.argv) != 3:
		print ("Modo correto de usar: script, IP Address, port number")
		exit()
	IP_Address = str(sys.argv[1])
	Port = int(sys.argv[2])
	server.bind((IP_Address, Port))
	server.listen(50)
	while True:	
		print ("Aguardando conecção...")
		cli_sock, cli_addr = server.accept()
		cli_sock.send('Bem vindo {}\n(Mensagem do sevidor)\n'.format(cli_addr).encode())
		list_client.add(cli_sock) #adicionar clientes a list_client
		print ("Conectado de: ", cli_addr[0])
		threading.Thread(target = messagem, args = (cli_sock, )).start()
	#while  True:
		#data = cli_sock.recv(1024)
		#if not data:
			#break
		#cli_sock.send(('[%s] %s' %bytes(ctime(), 'utf-8'), data))#(data.encode('utf-8'))
		#cli_sock.close()
server.close()

