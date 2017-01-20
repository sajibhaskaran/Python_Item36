import sqlite3
import time
import datetime as dt
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')



conn = sqlite3.connect('learning_test.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452123542, '2016-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = time.time()
    date = str(dt.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot(unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()

def read_from_db():
    c.execute("SELECT keyword, unix FROM stuffToPlot WHERE unix > 1452618731")
    data = c.fetchall()
    #print(data)
    for row in data:
        print(row)

def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []

    for row in c.fetchall():
        dates.append(dt.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


def del_and_update():

    
    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 8')
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]
    print(50 * '#')
    
    c.execute('DELETE FROM stuffToPlot WHERE value = 99')

    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]



create_table()

#read_from_db()
del_and_update()

'''
# data_entry()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
'''
#graph_data()
c.close()
conn.close()






























