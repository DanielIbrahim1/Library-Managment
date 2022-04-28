# Library-Managment

* Its my first project as a student of Python full stack bootcamp 
* In this project you can management your own library

* Here i will explain about the project, first off all the project divides for 3 section`s
1) book
2) customers
3) loans 

* every section had some function, so lets go. 

# books fucntion : 

1) def books() : in this function i build the books table with the follow column - Id*, Name, Author,Year Published, Status*
* Id- for book Id with autoincrement to avoid multiple id`s.
* Status- for each book status, to help the customers and you to know wich book is available and wich one is issued/

2) def addBook() : in this fucntion you can add book`s to the library, every column is required here to avoid errors.

3) def showBooks(): this fucntion helps to dispaly all the books in the library at the same time.

4) def deleteBook(): this fucntion helps to delete a book permanently from the library. 

5) def search book(): this function helps every customer to search for a book by it name`s, first

6) availBook(): this function helps to show just the available books in the lirbrary to avoid attempts to loan an issued book by the customers. 

# Customers section: 

1) def customers() : in this function i build the Customers table with the follow column - Id*, Name, City,Age
* Id- for book Id with autoincrement to avoid multiple id`s.

2) def addCustomer() : in this fucntion you can add customers to the DB, every column is required here to avoid errors.

3) def showCustomers(): this fucntion helps to dispaly all the customers in the library/DB at the same time.

4) def removeCustomer(): this fucntion helps to delete a Custoemr permanently from the DB. 

5) def searchCustomer(): this function helps every customer to search for a book by it name`s, first



# Loans section: 

1) def laons() : in this function i build the laons table with the follow column - CustID, BookID, LoanDate,returnDate*,Status.
* returnDate- its the supposed loan, and it depened on the book type

2) def loanBook() : in this fucntion you can loan a book from the library, every loan action will dispaly a msg that told the return date. every book can loaned by one customer at the same time until the customer return it.

3) def showAllLoans(): this fucntion helps to dispaly all the loans in the library/DB at the same time.

4) def issuedBooks(): this fucntion helps to display just the issued book`s, its and aid function for the return book.

5) def returnBook(): this function helps to return a book from customer to the library, and make it availabe to loan by other customer.

6) def LateLoans(): this fucntion disaplay all the late loans that didnt returned yet to the library. 

