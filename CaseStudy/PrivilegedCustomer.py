from CaseStudy.Customer import Customer

class RegularCustomer(Customer):
    def __init__(self,Customer,Address,memcardtype):
        self._customer = Customer
        self._address = Address
        self._memcardtype = memcardtype
        
    def setmemcardtype(self):
        self._memcardtype = 0.5
        
    def getmemcardtype(self):
        return self._memcardtype
    
    def displaycustomerinformstion(self):
        return self._Customer       

rc = RegularCustomer()
rc.setmemcardtype(input("Enter Card Type > "))