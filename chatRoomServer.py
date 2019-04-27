# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:56:16 2019

@author: M7md_Karam
"""
#For communication.
from socket import socket, AF_INET, SOCK_STREAM
#For Multi-threading.
from _thread import start_new_thread

def connectNewUser (c):
    #Sending the number of the client.
    start_msg = "You're client number "+str(clientNumber)
    c.send(start_msg.encode('UTF-8'))
    while True:
        m = c.recv(2048).decode('UTF-8')
        sendToAll(m,c)

clientNumber = 0
def getClientNumber (conn):
    global clientNumber
    clientNumber = 0
    for client in clients:
        clientNumber = clientNumber +1
        if client == conn:
            break;
        
def sendToAll(msg, con):
    getClientNumber (con)
    for client in clients:
        if client != con:
            specClientMsg = "Client"+str(clientNumber)+": "+msg
            client.send(specClientMsg.encode('UTF-8'))
            
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

#Creating a list for containing the sessions numbers provided for each client.
clients= []

while True:
    c, ad = s.accept()
    clients.append(c)
    getClientNumber(c)
    start_new_thread(connectNewUser, (c,))