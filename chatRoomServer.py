# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:56:16 2019

@author: M7md_Karam
"""

from socket import socket, AF_INET, SOCK_STREAM
from _thread import start_new_thread

s=socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 7010
s.bind((host, port))
s.listen(5)
print ("Server established")

clients= []

def connectNewUser (c):
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
            
            
while True:
    c, ad = s.accept()
    clients.append(c)
    getClientNumber(c)
    start_new_thread(connectNewUser, (c,))