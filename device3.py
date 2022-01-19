# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 21:25:44 2021

@author: Linda
"""
#%%
import DeviceTools as dt


#Genero delle misure random, il parametro indica la quantità di misure
dt.generateMeasures(4)
#Estrapola i dati dal file
dataPath = "DataDevice1.txt"
message = dt.getDataFromFile(dataPath)

#Indirizzi che mi servono per spedire i dati
myDevAddress = "192.168.1.4"
myDevSubnet= "255.255.255.0"
gatewayAddress = ("localhost", 6842)

#Spedisco i dati ricavati al gateway
dt.sendDataToGateway(myDevAddress,myDevSubnet,gatewayAddress, message)

