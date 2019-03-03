#by Cleitinho
"""class Chat:
	#@staticmethod
	#def showThalk():

	def countCarctersFile(file):
"""
import shutil
messages = ""

def limpar_terminal(menos_linhas = 0):
	colunas, linhas = shutil.get_terminal_size()

	for i in range(1,linhas - menos_linhas):
		print()

def update_terminal():
	while True:
		a = chat()
		if(a == "0"):
			break
		else:
			limpar_terminal()

def new_message(msg, autor = "unknouw"):
	global messages

	messages += autor + ": " + msg + "\n"
	print("concatenou messages = {}".format(messages))

def chat():
	global messages

	limpar_terminal()

	colunas, linhas = shutil.get_terminal_size()
	lines_msg = count_lines_msg(colunas)

	print(messages, end = "")

	if lines_msg < linhas:
		limpar_terminal(lines_msg + 1)

	text = input("digite alguma merda! (0 - Sair)\n")
	
	if text != "0":
		new_message(text)
	return text

def count_lines_msg(num_terminal_col):
	global messages

	num_lines = 0
	count_char = 0

	for i in messages:
		if i == "\n" or count_char >= num_terminal_col:
			num_lines = num_lines + 1
			count_char = 0
		else:
			count_char = count_char + 1

	return num_lines

if __name__ == '__main__':	
	update_terminal()
