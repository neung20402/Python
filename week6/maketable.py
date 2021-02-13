import sqlite3
conn = sqlite3.connect (r"C:\Users\acer\Documents\Sakphichet_Python\week6\work6.db")
c = conn.cursor()
c.execute ('''CREATE TABLE data (ID integer PRIMARY KEY AUTOINCREMENT,
    Name varchar(50) NOT NULL,
    Sex varchar(10) NOT NULL,
    Age varchar(10) NOT NULL,
    GradeYear varchar(10) NOT NULL,
    Email varchar(100) NOT NULL)''')
conn.commit()
conn.close()