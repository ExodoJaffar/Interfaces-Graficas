#-*-coding:utf8;-*-
#py:3.6

from tkinter import *
from tkinter import ttk

# Criando widget principal :
root = Tk()

# Criando botao para sair : 
ttk.Button(root, text='Exit',command=quit).pack()

# Iniciando widget principal
root.mainloop()

