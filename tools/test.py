

from flask import render_template


def testFunction():
    import sqlite3
    con = sqlite3.connect('library.db', check_same_thread=False) 
    cur=con.cursor()
    cur.execute('''INSERT INTO Books VALUES(not null, "Python full stack", "Eyal gold", 1994, 1, "avail")''')
    cur.execute('''INSERT INTO Books VALUES(not null, "Javascript for beginner", "Roy Abramovich", 2000, 2, "avail")''')
    cur.execute('''INSERT INTO Books VALUES(not null, "Data analyst", "Yoaed Baram", 1980, 3, "avail")''')
    cur.execute('''INSERT INTO Books VALUES(not null, "Hacking secerets", "Yishai 80", 1987, 1, "avail")''')
    cur.execute('''INSERT INTO Books VALUES(not null, "MySql learner", "Yael", 1998, 2, "avail")''')
    cur.execute('''INSERT INTO Books VALUES(not null, "Marketing methods", "Roy", 2007, 3, "avail")''')
    cur.execute('''INSERT INTO Customers VALUES(not null, "Daniel Ibrahim", "Tel aviv", 27)''')
    cur.execute('''INSERT INTO Customers VALUES(not null, "Chanel Poodle", "Tel aviv", 3)''')
    cur.execute('''INSERT INTO Customers VALUES(not null, "Oreo Poodle", "Ashdod", 18)''')
    cur.execute('''INSERT INTO Customers VALUES(not null, "Elza Poodle", "Shefa-amr", 88)''')
    cur.execute('''INSERT INTO Customers VALUES(not null, "Shelly Fiction", "Ashkelon", 29)''')
    con.commit()
# testFunction()

