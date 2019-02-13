import socket
HOST = ''              # Endereco IP do Servidor
PORT = 5002            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    print ('Conectado por', cliente)
    with open('database.txt', 'r+') as txt:
	    while True:
	        msg = con.recv(1024)
	        if not msg: break
	       	a = "{} : {}".format(cliente ,str(msg).replace('b',''))
	       	txt.write(f'{a}\n')
    print ('Finalizando conexao do cliente', cliente)
    con.close()