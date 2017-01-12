import sqlite3

connection = sqlite3.connect('test_database.db')

c = connection.cursor()
'''
c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")

c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)")

connection.commit()
'''
c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")

row= c.fetchone()
print(row)

