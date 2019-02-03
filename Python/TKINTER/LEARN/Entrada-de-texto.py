#-*-coding:utf8;-*-
#py:3.6

from tkinter import *

root = Tk()
soma = DoubleVar(root)
parcela = DoubleVar(root)
def aritmetica(e):
	soma.set(soma.get()+parcela.get())

lsoma= Label(textvar=soma)
entrada = Entry(textvar=parcela)
entrada.bind("<Return>", aritmetica)
lsoma.pack()
entrada.pack(side='bottom')
mainloop()

