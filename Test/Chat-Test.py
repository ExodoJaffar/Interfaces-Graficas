#-*-coding:utf8;-*-
#py:3.6
#tkinter:8.6.6

from tkinter import *
from tkinter import ttk

def enviar(e):
	texto.set(textoEnviar.get())


root = Tk()

texto = StringVar(root)
textoEnviar = StringVar(root)

textChat = ttk.Label(root, textvar=texto)
textChat.grid()

entrada = ttk.Entry(root,width = 100, textvar=textoEnviar)
entrada.bind("<Return>", enviar)
entrada.grid(column=4,row=1)

root.geometry('600x250+100+100')

mainloop()
