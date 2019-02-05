#-*-coding:utf8;-*-
#py:3.6
#tkinter:8.6.6

from tkinter import *

root = Tk()
write = StringVar(root)
log = Text(root, state='disabled', width=80, height=24, wrap='none')
log.grid()

b = Button(log, text='Push Me')
log.window_create('1.0', window=b)

def writeToLog(e):
	numlines = log.index('end - 1 line').split('.')[0]
	log['state'] = 'normal'
	if numlines == 24:
		log.delete(1.0,2.0)
	if log.index('end-1c') != '1.0':
		log.insert('end','\n')
	log.insert('end', write.get())
	log['state'] = 'disabled'

botao = Entry(root, textvar=write)
botao.bind('<Return>', writeToLog)
botao.grid()

mainloop()

