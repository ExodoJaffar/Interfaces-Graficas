try:
	import socket
except Exception as e:
	print(e)

tcp = None

def OpenConnect(destino:tuple):
	global tcp

	tcp =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.connect(destino)

def CloseConnect():
	global tcp

	tcp.close()

def SendMsg(msg):
	global tcp

	tcp.send(bytes(msg,'utf-8'))

if __name__ == '__main__':
	HOST = '127.0.0.1'     # Endereco IP do Servidor
	PORT = 5002            # Porta que o Servidor esta
	dest = (HOST, PORT)
	OpenConnect(dest)
	msg = input()
	while msg != "\x18":
		SendMsg(msg)
		msg = input()
	CloseConnect()

		