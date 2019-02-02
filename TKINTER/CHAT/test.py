#-*-coding:utf8;-*-
#py:3.6
from tkinter import *

class Aplicacao(Frame):
	def __init__(self, master= None):
		Frame.__init__(self, master)
		self.msg = Label(self, text="Hello")
		self.msg.pack ()


app = Aplicacao()
app.master.title('Chat Online')
app.master.geometry('650x300+200+200')
mainloop()

