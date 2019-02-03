#-*-coding:utf8;-*-
#py:3.6

from tkinter import *

def enviar(e):
	texto.set(textoEnviar.get())


root = Tk()
texto = StringVar(root)
textoEnviar = StringVar(root)
textChat = Label(textvar=texto)
entrada = Entry(textvar=textoEnviar)
entrada.bind("<Return>", enviar)
textChat.pack()
entrada.pack(side='bottom')
root.geometry('600x250+100+100')
mainloop()

