#-*-coding:utf8;-*-
#py:3.6
#tkinter:8.6.6

from tkinter import *

class Aplicacao(Frame):
	def __init__(self, master= None):
		Frame.__init__(self, master)
		self.msg = Label(self, text="Hello")
		self.msg.pack ()
		self.pack()


app = Aplicacao()
app.master.title('Chat Online')
app.master.geometry('650x250+200+200')
mainloop()

