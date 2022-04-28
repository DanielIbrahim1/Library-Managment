import sqlite3
from flask import Flask , render_template, json, request

class MyCustomers:
    con = sqlite3.connect('library.db', check_same_thread=False) 
    cur=con.cursor()
    #userCustomer=[]
    allCustomers=[]
    custID=[]
    def customers(self):
        try:
            self.cur.execute('''CREATE TABLE Customers(Id INTEGER PRIMARY KEY,Name varchar(30),City varchar(30),Age int) ''')
        except:
            print('Table already exist')
            self.con.commit()

    def addCustomer(self):
        self.msg=''
        if request.method=='POST':
            Name=request.form.get('Name')
            City=request.form.get('City')
            Age=request.form.get('Age')
            inserData=f"INSERT INTO Customers values(NOT NULL,'{Name}','{City}','{int(Age)}') "
            self.cur.execute(inserData)
            self.con.commit()
            self.msg='Customer has been added'
    
    def showCustomers(self):
        showData="SELECT * FROM Customers"
        self.cur.execute(showData)
        self.allCustomers=[]
        self.allCustomers=self.cur.fetchall()
        return self.allCustomers

    def removeCustomer(self):
        self.msg=''
        if request.method == 'POST':
            custmerID=request.form.get('Id')
            delCustomer=f"DELETE FROM Customers where Id='{custmerID}'"
            self.cur.execute(delCustomer)
            self.con.commit()
            self.msg='Customer has been added'


    def searchCustomer(self):
        self.userCustomer=[]
        if request.method == 'POST':
            Name=request.form.get('Name')
            findCust=f"SELECT * FROM Customers WHERE Name='{Name}'"
            self.cur.execute(findCust)
            self.userCustomer=self.cur.fetchall()
            return self.userCustomer          
    

    
    