from CaseStudy.Address import Address
from Main.py import *

class Customer:
    def __init__(self,customername,telephoneno,Address):
        self._customername=customername
        self._telephoneno = telephoneno
        self._address = Address
        print('Initialized!!!')
    
    def setcustomerid(self):
        self._customerid= 'C1'
        
    def setcustomername(self,customername):
        self._customername=customername
    
    def settelephoneno(self,tele):
        self._telephoneno=tele
    
    def setaddress(self,addr):
        self._Address=addr
        
    def getcustomerid(self):
        return self._customerid
    
    def gettelephoneno(self):
        return self._telephoneno
    
    def getcustomername(self):
        return self._customername 
    
    def getaddress(self):
        return self._Address


objAddress = Address('q','w','e','r','t')
c = Customer('id','name','1234',objAddress)