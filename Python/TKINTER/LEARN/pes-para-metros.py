#coding:utf8
#py:3.6
#tkinter:8.6

from tkinter import *
from tkinter import ttk

# Funcoes :
def calcular(*args):
	try:
		valor = float(pes.get())
		metros.set((0.3048 * valor * 10000.0 + 0.5)/10000.0)
	except Exception as e:
		pass

# Criando widgets : 
root = Tk()
root.title('Pes para metros')
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W , E , S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Criando variaveis : 
pes = StringVar()
metros = StringVar()

# Criando entradas : 
pes_entry = ttk.Entry(mainframe, width=7, textvariable=pes)
pes_entry.grid(column=2, row=1, sticky=(W, E))

# Iniciando Labels e Button : 
ttk.Label(mainframe, textvariable=metros).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calcular", command=calcular).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="pes").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="é igual a ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="metros").grid(column=3, row=2, sticky=W)

# Configurando child widgets do mainframe:
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# Declarando o foco :
pes_entry.focus()

root.bind("<Return>", calcular) # Se pressionado enter em qualquer parte do programa ira chamar a funcao calcular

# Iniciando aplicativo
root.mainloop()

