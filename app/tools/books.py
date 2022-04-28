
import sqlite3
from flask import Flask , render_template, json, request
# con = sqlite3.connect('library.db', check_same_thread=False) 
# cur=con.cursor()
from tkinter import *
from tkinter import messagebox

class MyBooks:
    con = sqlite3.connect('library.db', check_same_thread=False) 
    cur=con.cursor()
    #userBook=[]
    allBooks=[]
    availBooks=[]
    allBooks = []
    def books(self):
        try:
        # Create table
            self.cur.execute('''CREATE TABLE Books(Id INTEGER PRIMARY KEY,Name varchar(30),
            Author varchar(30),Year Published int,Type,Status varchar(30))''')
        except:
            print("table already exist")
        # Save (commit) the changes
        self.con.commit()
    


    def addBook(self):
        self.msg=''
        if request.method == 'POST':
            Name =request.form.get('Name')
            Author =request.form.get('Author')
            Year_Published =request.form.get('Year Published')
            Type =request.form.get('Type')
            Status =request.form.get('Status')
            sqlStr=f"INSERT INTO Books values(NOT NULL,'{Name}','{Author}',{int(Year_Published)},'{Type}','{Status}')"
            print(sqlStr)
            self.cur.execute(sqlStr)
            self.con.commit()
            self.msg='Book has been added'
            #messagebox.showinfo('Success',"Book added successfully")
        
        

    def showBooks(self):
        SQL = "SELECT *  FROM Books" # creating Variable that select from the created table (above)
        print(SQL)# printing 
        self.cur.execute(SQL)
        self.allBooks = []
        self.allBooks=self.cur.fetchall()
        # for i in self.cur:
        #     self.allBooks.append({"Id": i[0],"Name": i[1], "Author": i[2],
        #             "Year_Published": i[3],"Type": i[4], "Status": i[5]})
        return self.allBooks
        #(json.dumps(self.allBooks))
   
    def deleteBook(self):
        self.msg=''
        if request.method == 'POST':
            bookId=request.form.get('Id')
            sqlStr=f"DELETE FROM Books where Id='{bookId}'"
            print(sqlStr)
            self.cur.execute(sqlStr)
            self.con.commit()
            self.msg='Book has been deleted'
           # messagebox.showinfo('Success',"Book Deleted Successfully")

    def searchBook(self):
        self.userBook=[]
        if request.method == 'POST':
            bookName=request.form.get('Name')
            SQL = f"SELECT * FROM Books WHERE Name ='{bookName}'" 
            print(SQL)# printing 
            self.cur.execute(SQL)
            self.userBook=self.cur.fetchall()
            return self.userBook
        
    
    def availBook(self):
        SQL = "SELECT Id,Name FROM Books WHERE Status IN ('avail')" 
        print(SQL)# printing 
        self.cur.execute(SQL)
        self.con.commit()
        self.availBooks=self.cur.fetchall()
        return self.availBooks   
    

        # for i in self.cur:
        #         self.Row.append({"id":i[0],"Name":i[1],"Author":i[2],
        #          "Year_Published":i[3],"Type":i[4],})
            

        # def findBook(self):
        #     if request.method=='POST':
        #         bookName = request.form.get('bookName')
        #         bookAuthor=request.form.get('bookAuthor')
        #         sql = (f'''select * from books where bookName like "%{bookName}%" and Author like "%{bookAuthor}%"''')
        #         cur.execute(sql)
        #         books = cur.fetchall()
        #         return render_template("/books/findBook.html", books=books)
        #     return render_template("/books/findBook.html")

            
            
            
            # self.userBook=[]
            # for row in self.cur:
            #     self.userBook.append({"id":row[0],"Name":row[1],"Author":row[2],
            #     "Year_Published":row[3],"Type":row[4],})
            #     return self.userBook
            
        #print(self.cur)

          
            

   

 