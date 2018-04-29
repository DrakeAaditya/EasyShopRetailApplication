'''
Created on Apr 30, 2018

@author: addyr
'''
class Customer:
    def _init_(self,customerid,customername,telephoneno,addressid):
        self._customerid=customerid
        self._customername=customername
        self._telephoneno = telephoneno
        self._addressid = addressid

    def setcustomerid(self,cid):
        self._customerid=cid
        
    def setcustomername(self,customername):
        self._customername=customername
    
    def settelephoneno(self,tele):
        self._telephoneno=tele
    
    def setaddress(self,addr):
        self._addressid=addr
        
    def getcustomerid(self):
        return self._customerid
    
    def gettelephoneno(self):
        return self._telephoneno
    
    def getcustomername(self):
        return self._customername 
    
    def getaddress(self):
        return self._addressid
    

class Address(Customer):
    def __init__(self,addressid,addressLine,city,zipcode,state):
        self._addressid=addressid
        self._addressLine = addressLine
        self._city=city
        self._zipcode =zipcode
        self._state=state
        
    ty
    def setadddresLine(self,addre):
        self._addressLine=addre
        
    def setcity(self,city):
        self._city=city
        
    def setzipcode(self,zipcode):
        self._zipcode=zipcode
        
    def setstate(self,state):
        self._state=state
        
    def getaddressLine(self):
        return self._addressLine
        
    def getaddressid(self):
        return self._addressid
    
    def getcity(self):
        return self._city
    
    def getstate(self):
        return self._state
    
    def validzipcode(self):