from re import A
import sqlite3
from flask import Flask , render_template, json, request
import datetime

# import books
# import customers

class MyLoans:
    con = sqlite3.connect('library.db', check_same_thread=False) 
    cur=con.cursor()
    availBooks=[]
    allLoans=[]
    allIssuedBooks=[]
    allLoans=[]
    
    def laons(self):    
        try:
        # Create table
            self.cur.execute('''CREATE TABLE Loans(CustID INT,BookID INT,LoanDate INT,ReturnDate INT,Status text)''')
        except:
            print("table already exist")
        # Save (commit) the changes
        self.con.commit()


    def loanBook(self):
        self.msg=''
        if request.method == 'POST':
            CustID=request.form.get('CustID')
            BookID=request.form.get('BookID')
            loanDate=request.form.get('LoanDate')
            print(loanDate)
            status=(f'''UPDATE Books SET Status='issued' WHERE Id='{BookID}' ''')
            self.cur.execute(status)
            self.cur.execute(f"SELECT Type FROM Books WHERE Id='{BookID}'")
            booType=self.cur.fetchone()[0]
        # for bkType in self.cur:
        #     booType=bkType[0]
        #     print(booType)
            if( booType == '1'):
                date1=datetime.datetime.strptime(loanDate, "%Y-%m-%d")
                returnDate=(date1 + datetime.timedelta(days=10)).date()
                #returnDate = date2.date()
                self.cur.execute(f'''INSERT INTO Loans VALUES ('{CustID}','{BookID}','{loanDate}','{returnDate}','issued')''')
                self.msg=f"Book has been loaned for 10 days, until {returnDate}"
            elif (booType=='2'):
                date1=datetime.datetime.strptime(loanDate, "%Y-%m-%d")
                returnDate=(date1 + datetime.timedelta(days=5)).date()
                #returnDate = date2.date()
                self.cur.execute(f'''INSERT INTO Loans VALUES ('{CustID}','{BookID}','{loanDate}','{returnDate}','issued')''')
                self.msg=f"Book has been loaned for 5 days, until {returnDate}"
            elif (booType=='3'):
                date1=datetime.datetime.strptime(loanDate, "%Y-%m-%d")
                returnDate=(date1 + datetime.timedelta(days=2)).date()
                #returnDate =date2.date()
                self.cur.execute(f'''INSERT INTO Loans VALUES ('{CustID}','{BookID}','{loanDate}','{returnDate}','issued')''')
                self.msg=f"Book has been loaned for 2 days, until {returnDate}"
    #             loan=(f'''INSERT INTO Loans VALUES ('({CustID})','{BookID}','{loanDate}','{returnDate}','issued')''')
    #             self.cur.execute(loan)
            self.con.commit()
            



    def showAllLoans(self):
        showData="SELECT *  FROM Loans"
        self.cur.execute(showData)
        self.allLoans=self.cur.fetchall()
        return self.allLoans

    
    def issuedBooks(self):
        SQL = "SELECT Id,Name,Type FROM Books WHERE Status IN ('issued')" 
        print(SQL)# printing 
        self.cur.execute(SQL)
        self.con.commit()
        self.allIssuedBooks=self.cur.fetchall()
        return self.allIssuedBooks   
    

  
    def returnBook(self):
        self.msg=''
        if request.method=='POST':
            BookID=request.form.get('BookID')
            #returnDate=request.form.get('ReturnDate')
            loansbook=(f"UPDATE Loans SET Status='Returned' WHERE BookID='{BookID}'")
            self.cur.execute(loansbook)
            returnedBook=(f"UPDATE Books SET Status='avail' WHERE Id='{BookID}'")
            self.cur.execute(returnedBook)
            # retDate=(f"UPDATE Loans SET ReturnDate='{returnDate}'")
            # self.cur.execute(retDate)
            self.con.commit()
            self.msg='Book has been returned'


    def LateLoans(self):
        SQL2= ''' SELECT Customers.Name,Books.Name,LoanDate,ReturnDate
                FROM Loans
                INNER JOIN Books ON Books.Id=Loans.BookID
                INNER JOIN Customers ON Loans.CustID=Customers.Id
                WHERE Loans.Status="issued"
                '''
        self.cur.execute(SQL2)
        self.con.commit()
        self.allLoans=self.cur.fetchall()
        self.allLateLoans=[]
        self.lateDays=[]
        for late in self.allLoans:
            returnedDate=(datetime.datetime.strptime(late[3], "%Y-%m-%d"))
            print(returnedDate)
            today=datetime.datetime.today()
            print(today)
            self.result=(today-returnedDate)
            if (self.result.days > 0):
                self.allLateLoans.append(late)
                
                
               
            
        
        
                    
        
#   for late in self.allLoans:
#             returnedDate=(datetime.datetime.strptime(late[3], "%Y-%m-%d"))
#             print(returnedDate)
#             today=datetime.datetime.today()
#             print(today)
#             self.result=(today-returnedDate) 
#             if (self.result.days > 0):
#                 self.allLateLoans.append(late)
#         return self.allLateLoans
        

        # SQL1="SELECT ReturnDate FROM Loans WHERE Status IN ('issued')"
        # self.cur.execute(SQL1)
        # returnedBook=self.cur.fetchone()[0]
        # print(returnedBook)
        # returnedDate=datetime.datetime.strptime(returnedBook, "%Y-%m-%d")
        # today=datetime.datetime.today()
        # result=(today-returnedDate)
        # if ( result.days < 0):
        #     SQL2= ''' SELECT Customers.Name,Books.Name,LoanDate,ReturnDate
        #         FROM Loans
        #         INNER JOIN Books ON Books.Id=Loans.BookID
        #         INNER JOIN Customers ON Loans.CustID=Customers.Id
        #         WHERE Loans.Status="issued"
        #         '''
        #     self.cur.execute(SQL2)
        #     self.con.commit()
        #     self.allLateLoans=self.cur.fetchall()
        
        # SQL2= ''' SELECT Customers.Name,Books.Name,LoanDate,ReturnDate
        #         FROM Loans
        #         INNER JOIN Books ON Books.Id=Loans.BookID
        #         INNER JOIN Customers ON Loans.CustID=Customers.Id
        #         WHERE Loans.Status="issued"
        #         '''
        # self.cur.execute(SQL2)
        # self.con.commit()
        # self.allLateLoans=self.cur.fetchall()
