# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 12:54:51 2019

@author: M7md_Karam
"""
from tkinter import Label, Entry, Tk, END, Button
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

def receive_thread(s):
    while True:
        x=s.recv(500).decode('UTF-8')
        if lbl["text"]=="Nothing received":
            lbl["text"]="Server: "+x
        else:
            lbl["text"]=lbl["text"]+"\n"+"Server: "+x

def send_function():    
    x = en.get()
    if lbl["text"]=="Nothing received":
        lbl["text"]="Client: "+x
    else:
        lbl["text"]=lbl["text"]+"\n"+"Client: "+x
    s.send(x.encode('UTF-8'))
    en.delete(0,END)
    
wind = Tk()
wind.title ("Client Side")
wind.geometry ('600x400')
en = Entry (wind,width=30)
en.grid (column = 0, row=1)

btn = Button (wind,text="Send",width=33, height=1, command = send_function)
btn.grid(column=1, row=2)

lbl= Label(wind, text="Nothing received",font=('Helvertica','15'))
lbl.grid(row=3, column=1)

s=socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1',7010))
receive=Thread(target=receive_thread,args=(s,))
receive.start()

wind.mainloop()