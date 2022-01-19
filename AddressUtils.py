# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 21:23:48 2021

@author: Linda
"""

class AddressTools:
    def __address_splitter(self, ip):
        bytesList = []
        for x in ip.split("."):
            bytesList.append(int(x))
        return bytesList

    def __init__(self, ip, subnet):
        self.ip = ip
        self.subnet = subnet
        self.ip_octets = self.__address_splitter(ip)
        self.subnet_octets = self.__address_splitter(subnet)

    def getAddressEncoded(self):
        return bytes(self.ip_octets) + bytes(self.subnet_octets)

    def convertBytesToIP(ipBytes, subnetBytes):
        ipTemp = ''
        subnetTemp = ''
        for i in range(4):
            ipTemp += str(ipBytes[i]) + ('.' if i < 3 else '')
            subnetTemp += str(subnetBytes[i]) + ('.' if i < 3 else '')
        return AddressTools(ipTemp, subnetTemp)