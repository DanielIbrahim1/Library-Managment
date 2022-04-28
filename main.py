import imp
from flask import Flask , render_template, json, request
api = Flask(__name__)
import tools.books as Books # importimg books module with alias 
import tools.customers as Customers # importimg customers module with alias
import tools.loans as loans
booksT=Books.MyBooks() #Placement MyBooks class (books table management) as booksT
customersT=Customers.MyCustomers() #Placement MyCustomer class (Customers table management) as customersT
loansT=loans.MyLoans()
import tools.test as Test

@api.route('/', methods=['GET', 'POST'])
def home_page():
    booksT.books()
    loansT.laons()
    customersT.customers()
    # Test.testFunction()
    return render_template('home.html' )

# @api.route('/', methods=['GET', 'POST'])
# def add_data():
#     return Test.testFunction()


@api.route('/addbook', methods=['GET', 'POST'])
def add_Book_flask():
    booksT.books()
    booksT.addBook()
    msg=booksT.msg
    return render_template('addBook.html',msg=msg )


@api.route('/Books', methods=['GET', 'POST'])
def get_Books():
    booksT.showBooks()
    allBooks=booksT.allBooks
    #(json.dumps(allBooks))
    return render_template('allBooks.html', allBooks=allBooks)


@api.route('/delBook', methods=['GET', 'POST'])
def delete_a_book():
    booksT.deleteBook()
    booksT.showBooks()
    msg=booksT.msg
    allBooks=booksT.allBooks
    return render_template('deleteBook.html', msg=msg, allBooks=allBooks)

@api.route('/searchBook', methods=['GET', 'POST'])
def find_aBook():
    booksT.searchBook()
    print(booksT.userBook)
    userBook=booksT.userBook
    return render_template('findBook.html', userBook=userBook)


########################

@api.route('/addCustomer', methods=['GET', 'POST'])
def add_Customer():
    customersT.customers()
    customersT.addCustomer()
    msg=customersT.msg
    return render_template('addCustomer.html',msg=msg)


@api.route('/customers', methods=['GET', 'POST'])
def get_Customers():
    customersT.customers()
    customersT.showCustomers()
    allCustomers=customersT.allCustomers
    #(json.dumps(allBooks))
    return render_template('allCustomers.html', allCustomers=allCustomers)


@api.route('/delcustomer', methods=['GET', 'POST'])
def delete_a_Customer():
    customersT.customers()
    customersT.removeCustomer()
    customersT.showCustomers()
    msg=customersT.msg
    allCustomers=customersT.allCustomers
    return render_template('deleteCustomer.html',msg=msg,allCustomers=allCustomers)

@api.route('/searchCustomer', methods=['GET', 'POST'])
def find_a_Customer():
    customersT.customers()
    customersT.searchCustomer()
    print(customersT.userCustomer)
    userCustomer=customersT.userCustomer
    return render_template('findCustomer.html', userCustomer=userCustomer)



##############

@api.route('/loanbook', methods=['GET', 'POST'])
def loan_a_book():
    loansT.laons()
    loansT.loanBook()
    booksT.availBook()
    customersT.showCustomers()
    loansT.showAllLoans()
    availBooks=booksT.availBooks
    allCustomers=customersT.allCustomers
    msg=loansT.msg
    return render_template('loanBook.html', availBooks=availBooks,allCustomers=allCustomers,msg=msg)


@api.route('/loans', methods=['GET', 'POST'])
def show_all_loans():
    loansT.laons()
    loansT.showAllLoans()
    allLoans=loansT.allLoans
    #(json.dumps(allBooks))
    return render_template('allLoans.html', allLoans=allLoans)

@api.route('/return', methods=['GET', 'POST'])
def return_a_book():
    # loansT.laons()
    loansT.returnBook()
    loansT.issuedBooks()
    issuedBooks=loansT.allIssuedBooks
    msg=loansT.msg
    return render_template('returnBook.html', issuedBooks=issuedBooks,msg=msg )


@api.route('/lateloans', methods=['GET', 'POST'])
def show_all_late_loans():
    # loansT.laons()
    # loansT.returnBook()
    # loansT.issuedBooks()
    loansT.LateLoans()
    # customersT.customers()
    # booksT.books()
    allLateLoans=loansT.allLateLoans
    lateDays=loansT.lateDays
    return render_template('lateLoans.html', allLateLoans=allLateLoans,lateDays=lateDays )

# # #to apply the test function go to test.py and remove the '#' symbol
# def programTest():
#     return Test.testFunction()

#debug mode:
if __name__ == '__main__':
    api.run(debug="True",port=5000)

