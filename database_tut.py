import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Anydatas(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

'''
def data_entry():
    c.execute("INSERT INTO anyData VALUES(145123642, '2016-02-01', 5)")
    conn.commit()
    c.close()
    conn.close()
'''
def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H: %M: %S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    c.execute("INSERT INTO Anydatas (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
               (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    c.execute("SELECT * FROM Anydatas")
    for row in c.fetchall():
        print(row[0], row[2])

    

##create_table()
##
##for i in range(10):
##    dynamic_data_entry()
##    time.sleep(1)

read_from_db()

c.close()
conn.close()

