# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:13:17 2019

@author: M7md_Karam
"""

#For GUI.
from tkinter import Tk, Button, Label, Entry, END
#For Communication.
from socket import socket, AF_INET, SOCK_STREAM
#For Multi-threading.
from threading import Thread

def receive_thread(s):
    while True:
        x=s.recv(500)
        x=x.decode('UTF-8')
        if lbl["text"]=="Nothing received":
            lbl["text"]=x
        else:
            lbl["text"]=lbl["text"]+"\n"+x
            
def send_function(*args):
    x = en.get()
    lbl["text"]=lbl["text"]+"\n"+"Me: "+x
    s.send(x.encode('UTF-8'))
    en.delete(0,END)
    
wind = Tk()
wind.title ("Chat Member")
wind.geometry ('600x400')
wind.config(background="#222222")

en = Entry (wind,width=48,bg="#222222",fg="#dddddd",font=('Comic Sans MS','15'))
en.grid (column = 0, row=1, pady=1, padx = 10)
en.bind("<Return>", send_function)

btn = Button (wind,text="Send",width=10, height=1, bg="#222222",fg="#dddddd", font=('Comic Sans MS','15'), command = send_function)
btn.grid(column=0, row=2,padx=42, pady=1)

lbl= Label(wind, text="Nothing received",bg="#222222",fg="#dddddd",font=('Comic Sans MS','15'))
lbl.grid(row=3, column=0)

s=socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1',7010))
receive=Thread(target=receive_thread,args=(s,))
receive.start()

wind.mainloop()