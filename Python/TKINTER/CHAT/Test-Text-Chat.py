#-*-coding:utf8;-*-
#py:3.6
#tkinter:8.6.6

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Chat Online")
mainframe = ttk.Frame(root, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W , E , S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

write = StringVar()

log = Text(mainframe, state='disabled', width=80, height=24, wrap='none')
log.grid(column=1, row=1)

#b = Button(log, text='Push Me')
#log.window_create('1.0', window=b)

def writeToLog(e):
	numlines = log.index('end - 1 line').split('.')[0]
	log['state'] = 'normal'
	if numlines == 24:
		log.delete(1.0,2.0)
	if log.index('end-1c') != '1.0':
		log.insert('end','\n')
	log.insert('end', write.get())
	log['state'] = 'disabled'

entrada = ttk.Entry(mainframe, width=107, textvar=write)
entrada.bind('<Return>', writeToLog)
entrada.grid(column=1, sticky=W)

mainloop()

