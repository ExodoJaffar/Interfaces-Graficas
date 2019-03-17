#-*-coding:utf8;-*-
#py:3.6
#tkinter:8.6.6

from tkinter import *
from tkinter import ttk

# Functions : 
def aritmetica(e):
	soma.set(soma.get()+parcela.get())

# Criando widget principal : 
root = Tk()

# Criando variaveis :
soma = DoubleVar() 
parcela = DoubleVar()

# Criando widgets : 
lsoma= Label(root, textvar=soma)
entrada = Entry(root, textvar=parcela)
entrada.bind('<Return>', aritmetica) # ????

# Iniciando widgets com grid :
lsoma.grid()
entrada.grid()

# Iniciando widget principal : 
root.mainloop()

