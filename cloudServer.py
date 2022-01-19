# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:24:50 2021

@author: Linda
"""
#%%

from socket import *

def gatewayConnection():
    #creazione del socket del server
    serverConn = socket(AF_INET, SOCK_STREAM)

    #associo al mio socket un ip e una porta
    serverConn.bind(("localhost", sPort))
    
    #mi metto in ascolto delle richieste dei device
    serverConn.listen(1)
    print("*** CLOUD SERVER ***")
    print("Waiting for response on interface 10.10.10.0 : port {}..." .format(sPort))
    
    #attendo per la connessione del gateway
    gatewayConn, address = serverConn.accept()
    print("Success! Connection with the gateway done!")
    try:
        #TCP Server socket
        print("Data from each device :\n")
        message = gatewayConn.recv(buffer)
        print(message.decode("utf8"))
        gatewayConn.send(("Ok, all data received!").encode())       
    except Exception as e:
        print(e)
    finally:
        gatewayConn.close()
        serverConn.close()
        
#---CLOUDSERVER---#
sPort = 6123
sIP = '10.10.10.69'
buffer = 2048
gatewayConnection()