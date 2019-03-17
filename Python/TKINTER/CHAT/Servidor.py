try:
	import socket
except Exception as e:
	print(e)
tcp = None
con = None

def StartServer(origem:tuple):
	global tcp

	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.bind(origem)
	tcp.listen(1)

def GetMsg():
	msg = con.recv(1024)

	return str(msg).split("'")[1]

def WriteChat():
	with open('chat.txt', 'r+') as txt:
		while True:
			msg = GetMsg()
			if msg == '': break
			txt.write(f'{msg}\n')

def ConnectClient():
	global tcp
	global con

	con, cliente = tcp.accept()

	#return cliente

def CloseClient():
	con.close()

if __name__ == '__main__':
	HOST = ''              # Endereco IP do Servidor
	PORT = 5002            # Porta que o Servidor esta
	orig = (HOST,PORT)
	StartServer(orig)
	while True:
		ConnectClient()
		WriteChat()
	CloseClient()
