# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 21:27:48 2021

@author: Linda
"""

from random import *
from socket import *
from AddressUtils import *
import time

def generateMeasures(q):
    path="Data/DataDevice"
    for i in range(4):
        temp=path+str(i)+".txt"
        data=createRandomData(q)   
        with open(temp,"w") as f:
            f.write(data)   

def createRandomData(q):
    output=""
    temp=0
    offset=(24/q)-1
    for x in range(q):
        line= ("{}:00 - {} - {}%\n".format(randint(0+temp,1+temp),randint(25, 45),randint(15, 60)))
        temp+=offset
        output+=line
    return output

def getDataFromFile(path):
    fileTemp = "Data/" + path
    print("Reading the measures from file, please wait")

    with open(fileTemp, "r") as f:
        output = f.read()

    print("Done! Here we have the measures :\n")
    print(output) 
    print("--------------------\n")
    return output
    
#Mando le informazioni al gateway
def sendDataToGateway(myDevAddress,myDevSubnet,gatewayAddress, message):
    ip=myDevAddress
    subnet=myDevSubnet
    
    myAddTool= AddressTools(ip,subnet)
    output= myAddTool.getAddressEncoded()+message.encode("utf-8")
    
    #Creazione del socket UDP
    socketConn = socket(AF_INET, SOCK_DGRAM)
    buffer = 1024
    try:
        print("Sending data to Gateway on interface 192.168.1.0")
        initialTime = time.perf_counter()
        
        socketConn.sendto(output, gatewayAddress)
        print("Waiting the Gateway response...")
        data, server = socketConn.recvfrom(buffer)
        elapsedTime = round(time.perf_counter() - initialTime,3)
        print("Received Message: {}" .format(data.decode("utf8")))
        print("UDP connection took {} seconds with buffer size = {}" .format(elapsedTime, buffer))
    except Exception as e:
        print(e)
    finally:
        print("Closing Socket")
        socketConn.close()