from tkinter import *
from tkinter import ttk
from time import sleep
from Json import *

def Verificar(e=None):
	json = readJson()['Contas']
	if (nick.get() != '') and (password.get() != ''):
		
		try:
			if (password.get() == json[nick.get()]):
				clear()
				verif['text'] = ''
			else: verif['text'] = 'Dados Errado ou não inserido no banco de dados!\nDigite novamente, caso queira salvar essa conta.'
		except Exception as e:
			verif['text'] = 'Dados Errado ou não inserido no banco de dados!\nDigite novamente, caso queira salvar essa conta.'
	else:
		verif['text'] = 'Por Favor!\nDigite algo!'

def clear(a=None):
	login.place_forget()
	passw.place_forget()
	name.place_forget()
	pword.place_forget()
	push.place_forget()
	p = ttk.Progressbar(root, orient=HORIZONTAL, length=200, mode='determinate')
	p.place(x=25,y=50)


root     = Tk()
root.geometry('265x125')
root.title('Tela de Login')
root.bind("<Return>", Verificar)

nick     = StringVar(root)
password = StringVar(root)

login    = ttk.Label(root, text="Login")
login.place(x=40, y=40)

passw    = ttk.Label(root, text='Password')
passw.place(x=30, y=60)

verif = ttk.Label(root, text='')
verif.place(x = 1, y = 1)

name     = ttk.Entry(root, textvariable=nick, width=20)
name.place(x = 90,y = 35)

pword    = ttk.Entry(root, textvariable=password, width=20)
pword['show'] = '*'
pword.place(x = 90, y = 60)

push     = ttk.Button(root, text="Enviar Login", command=Verificar,width=20)
push.place(x= 88, y = 85)

