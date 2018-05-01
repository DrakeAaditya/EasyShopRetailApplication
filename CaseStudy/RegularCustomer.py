from CaseStudy.Customer import Customer

class RegularCustomer(Customer):
    def __init__(self,customername,telephoneno,Address,discount):
        super.__init__(customername,telephoneno,Address)
        self._discount = discount
        
    def setdiscount(self):
        self._discount = 0.5
        
    def getdiscount(self):
        return self._discount
    
    def displaycustomerinformstion(self):
        return self._Customer       