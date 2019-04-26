# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:13:17 2019

@author: M7md_Karam
"""

from tkinter import Tk, Label, Button, Entry, END
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

wind = Tk()


def receive_thread(s):
    while True:
        x=s.recv(500)
        x=x.decode('UTF-8')
        if lbl["text"]=="Nothing received":
            lbl["text"]=x
        else:
            lbl["text"]=lbl["text"]+"\n"+x
            


def send_function(*args):
    y = en.get()
    if lbl["text"]=="Nothing received":
        lbl["text"]=y
    else:
        lbl["text"]=lbl["text"]+"\n"+"Me: "+y
    s.send(y.encode('UTF-8'))
    en.delete(0,END)
    
wind.title ("Chat Room")
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