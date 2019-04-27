# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:06:21 2019

@author: M7md_Karam
"""
#For GUI.
from tkinter import Tk, Button, Label, Entry
#For Communication.
from socket import socket, AF_INET, SOCK_STREAM
#For Multi-threading.
from _thread import start_new_thread

def receive_thread(c):
    while True:
        x = c.recv(500).decode('UTF-8')
        #Concatenate the previously sent and received messages with the new message.
        lbl["text"]=lbl["text"]+"\n"+"Client: "+x

def client_thread():
    x=en.get()
    #Making sure it's the first message to send before deleting the nothing was sent message.
    if lbl["text"]=="Nothing was sent":
        lbl["text"]="Server: "+x
    else:
        #Concatenate the previously sent and received messages with the new message.
        lbl["text"]=lbl["text"]+"\n"+"Server: "+x
    c.send(x.encode('UTF-8'))

#Creating an empty window to contain all other objects.
wind = Tk()
#Setting the title of the window.
wind.title ("Server Side")
#Dimensions configuration.
wind.geometry ('600x400')

#Creating an entry for involving text to send.
en = Entry (wind,width=30)
#Positioning the entry in the second row, first column.
en.grid (row=1, column = 0)

#Create a button.
btn = Button (wind,text="Send",width=10, height=1, command = client_thread)
#Positioning the button in a grid in the third row, and first column.
btn.grid(row=2, column=0)

#Create a text label.
lbl= Label(wind, text="Nothing was sent",font=('Helvertica','15'))
#Positioning the label in a grid in the forth row, and first column.
lbl.grid(row=3, column=0)

#Creating an unbounded socket.
s=socket(AF_INET, SOCK_STREAM)
#Defining the server's IP.
host = '127.0.0.1'
#Defining the server's port number of the service.
port = 7010
#Binding both IP and port number to each other.
s.bind((host, port))
#Waiting for a client to connect.
s.listen(5)
print ("Server established")
#Infinite loop.
while True:
    #Accept a request for connection from a client,
    #return both session number, and information about the connected client (IP and port number)
    c, add=s.accept()
    print("connection from", add[0])
    #create thread for serving that session.
    start_new_thread(receive_thread,(c,))

    #Start the display of the GUI.
    wind.mainloop()