class Address:
    def __init__(self,addressid,addressLine,city,zipcode,state):
        self.__addressid=addressid
        self.__addressLine = addressLine
        self.__city=city
        self.__zipcode =zipcode
        self.__state=state
        
    def setadddresLine(self,addre):
        self.__addressLine=addre
        
    def setcity(self,city):
        self.__city=city
        
    def setzipcode(self,zipcode):
        self.__zipcode=zipcode
        
    def setstate(self,state):
        self.__state=state
        
    def getaddressLine(self):
        return self.__addressLine
        
    def getaddressid(self):
        return self.__addressid
    
    def getcity(self):
        return self.__city
    
    def getstate(self):
        return self.__state
    
    def validzipcode(self):
        return self.__zipcode