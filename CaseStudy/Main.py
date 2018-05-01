import mysql.connector
connection = mysql.connector.connect(host='localhost',database='easyshop',user='root',password='aaditya')
cur = connection.cursor();


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
    customername = input("Enter Customer Name > ")
    tele = input("Enter Customer Telephone Number > ")
    print("Enter Address")
    addre = input("Enter Address Line > ")
    city = input("Enter City > ")
    zipcode = input("Enter ZipCode > ")
    state = input("Enter State")
    customertype = input("Enter Customer Type > ")
if (choice == 2):
    subchoice = input("Enter Sub Choice > ")
    if (subchoice == 'a'):
        newcustomername = input("Enter New Name > ")
    if (subchoice == 'b'):
        newcustomertele = input("Enter New Telephone No. > ")
    if (subchoice == 'c'):
        print("Enter New Address")
        newaddre = input("Enter New Address Line > ")
        newcity = input("Enter New City > ")
        newzipcode = input("Enter New ZipCode > ")
        newstate = input("Enter New State")
    if (subchoice == 'd'):
        newcustomertype = input("Enter New Customer Type > ")
    if (subchoice == 'e'):
        newdiscount = float(input("Enter new Discount"))
    if (subchoice == 'f'):
        if(newcustomertype == 'Regular'):
            print("No Card Type Available for You")
        if(newcustomertype == 'Priviledged'):
            newmemcardtype = input("Enter New Membership Card Type > ")
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
    