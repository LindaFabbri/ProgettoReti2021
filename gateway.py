# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 21:24:48 2021

@author: Linda
"""
#%%

from AddressUtils import *
import time
from socket import *

def sendToCloudServer(m):   
    PORT=6123
    BUFFER = 1024
    print("Trying to connect to Cloud Server on port {}".format(PORT))
    try:
        socket_cloud = socket(AF_INET, SOCK_STREAM)
        socket_cloud.connect(('localhost', PORT))
        initialTime = time.perf_counter()
        socket_cloud.send(m.encode())
        data = socket_cloud.recv(BUFFER)
        print("Waiting the Cloud Server's answer...")
        elapsedTime = round(time.perf_counter() - initialTime,5)
        print("Received message: {}" .format(data.decode("utf8")))
        print("TCP message's sending time {} and the size of used buffer is {}" .format(elapsedTime, BUFFER))      
    except Exception as e:
        print(e)
    finally:
        print("Closing connection")
        socket_cloud.close()

def startGateway():
    m=""
    N_DEVICE=int(4)
    socketDev = socket(AF_INET, SOCK_DGRAM)
    socketDev.bind(("localhost",6842))
    print('*** Running *** --  Listening for devices...')
    
    #Aspetto di ricevere tutti i dati da tutti i socket
    devListened=list()
    try:
        #Continuo ad ascoltare finchè la mia lista non è piena di tutti i device
        while len(devListened)<N_DEVICE:

            data, address = socketDev.recvfrom(1024)
            deviceIP=AddressTools.convertBytesToIP(data[:4],data[4:8])
            deviceData=(data[8:]).decode("utf8")

            #Controllo se un device è già nella mia lista o se la subnet è diversa da 255.255.255.0
            if (deviceIP.subnet!="255.255.255.0") or (deviceIP.ip not in devListened):
                devListened.append(deviceIP.ip)
                indexDev=len(devListened)
                mReply = "Data arrived"
                print("The {}° IoT device has the following ip : {}".format(str(indexDev),deviceIP.ip))
                socketDev.sendto(mReply.encode(), address)
                #FRiempio il messaggio finale con i dati
                for line in deviceData.split('\n'):
                    if(line!=""):
                        m+=("{} - {}\n".format(deviceIP.ip,line))
    except Exception as e:
        print(e)
    finally:
        socketDev.close()   
    print("Data delivered!") 
    return m
   

#---GATEWAY---#
dataToSend=startGateway()
sendToCloudServer(dataToSend)