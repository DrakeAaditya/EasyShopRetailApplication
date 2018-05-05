from CaseStudy.Address import Address
import mysql.connector
connection = mysql.connector.connect(host='localhost',database='easyshop',user='root',password='aaditya')
cur = connection.cursor();

class Customer:
    def __init__(self,customername,telephoneno,Address):
        self.__customername=customername
        self.__telephoneno = telephoneno
        self.__address = Address
        print('Initialized!!!')
    
    def setcustomerid(self):
        self.__customerid= 'C1'
        
    def setcustomername(self,customername):
        self.__customername=customername
    
    def settelephoneno(self,tele):
        self.__telephoneno=tele
    
    def setaddress(self,addr):
        self.__Address=addr
        
    def getcustomerid(self):
        return self.__customerid
    
    def gettelephoneno(self):
        return self.__telephoneno
    
    def getcustomername(self):
        return self.__customername 
    
    def getaddress(self):
        return self.__Address



print("********************************************************")
print("\t\t\tEasy Shop")
print("********************************************************")
print("   1. Add New Customer")
print("   2. Modify\n\ta. Customer Name\n\tb. Customer Contact\n\tc. Customer Address\n\td. Customer Type\n\te. Discount %\n\tf. Membership Card Type")
print("   3. View All Customer")
print("   4. View All Regular Customer")
print("   5. View All Privileged Customer")
print("   6. Exit")

choice = int(input("\nEnter your choice > "))
print(choice)

if (choice == 1):
    x = input("Enter Customer Name > ")
    y = input("Enter Telephone Number > ")
    #c1 = Customer.setcustomername(x)
    #c2 = Customer.settelephoneno(input("Enter Telephone Number > "))
    
    print("Enter Address")
    address = input("Enter Address Line > ")
    city1 = input("Enter City > ")
    zipcode1 = input("Enter ZipCode > ")
    state1 = input("Enter State > ")
    #c3 = Customer.setaddress(address,city1,zipcode1,state1)
    z = Address('',address,city1,zipcode1,state1)
    cus = Customer(x,y,z)
    
    customertype1 = input("Enter Customer Type > ")
    if (customertype1 == 'Privileged'):
        memcardtype1 = input("Enter Membership Card Type > ")
    else:
        memcardtype1 = ""
    discount1 = input("Enter Discount > ")
    
    cur.execute("""INSERT INTO customer(customerid,customername,telephoneno,customertype,discount,memcardtype)
                VALUES('',%s,%s,%s,%s,%s)""",(cus.getcustomername(),cus.gettelephoneno(),customertype1,discount1,memcardtype1))
    connection.commit()
    
    cur.execute("""INSERT INTO address(addressline,city,zip,state,addressid) 
                VALUES(%s,%s,%s,%s,(SELECT addressid FROM customer WHERE customername = %s)))""",
                (z.getaddressLine(),z.getcity(),z.validzipcode(),z.getstate(),cus.getcustomername()))
    connection.commit()
    
    #customertype1 = input("Enter Customer Type > ")
if (choice == 2):
    upid = input("Enter Customer Id to be updated > ")
    subchoice = input("Enter Sub Choice > ")
    if (subchoice == 'a'):
        newcustomername = input("Enter New Name > ")
        cur.execute("UPDATE customer SET customername = %s WHERE customerid = %s",newcustomername,upid)
    if (subchoice == 'b'):
        newcustomertele = input("Enter New Telephone No. > ")
        cur.execute("UPDATE customer SET telephoneno = %s WHERE customerid = %s",newcustomertele,upid)
    if (subchoice == 'c'):
        print("Enter New Address")
        newaddre = input("Enter New Address Line > ")
        newcity = input("Enter New City > ")
        newzipcode = input("Enter New ZipCode > ")
        newstate = input("Enter New State > ")
        cur.execute("""UPDATE address SET addressline = %s,city = %s,zip = %s,state = %s WHERE 
                    addressid = (SELECT addressid FROM customer WHERE customerid = %s)""",newaddre,newcity,newzipcode,newstate,upid)
    if (subchoice == 'd'):
        newcustomertype = input("Enter New Customer Type > ")
        cur.execute("UPDATE FROM customer SET customertype = %s WHERE customerid = %s",newcustomertype,upid)
    if (subchoice == 'e'):
        newdiscount = float(input("Enter new Discount > "))
        cur.execute("UPDATE FROM customer SET discount = %s WHERE customerid = %s",newdiscount,upid)
    if (subchoice == 'f'):
        if(newcustomertype == 'Regular'):
            print("No Card Type Available for You")
        if(newcustomertype == 'Privileged'):
            newmemcardtype = input("Enter New Membership Card Type > ")
            cur.execute("UPDATE FROM customer SET memcardtype = %s WHERE customerid = %s",newmemcardtype,upid)
if(choice == 3):
    cur.execute("SELECT * FROM customer")
    for row in cur.fetchall():
        print(row)
if(choice == 4):
    cur.execute("SELECT * FROM customer WHERE customertype ='Regular'")
    for row in cur.fetchall():
        print(row)
if(choice == 5):
    cur.execute("SELECT * FROM customer WHERE customertype ='Privileged'")
    for row in cur.fetchall():
        print(row)
if(choice == 6):
    exit(0)
    
connection.close()