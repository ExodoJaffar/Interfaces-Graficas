#-*-coding=utf8
#py:3.6

from tkinter import *

class Aplicacao(Frame):
	"""docstring for Aplicacao"""
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.msg = Label(self, text="Hello World!")
		self.msg.pack()
		self.bye = Button(self, text='Bye', command=self.quit)
		self.bye.pack()
		self.pack()

app = Aplicacao()
app.master.title('Hello World')
app.master.geometry('650x250+200+200')
mainloop()