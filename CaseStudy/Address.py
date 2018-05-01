class Address:
    def __init__(self,addressid,addressLine,city,zipcode,state):
        self._addressid=addressid
        self._addressLine = addressLine
        self._city=city
        self._zipcode =zipcode
        self._state=state
        
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
        return self._zipcode