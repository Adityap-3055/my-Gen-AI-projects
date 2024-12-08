import sqlite3


## Connect to sqlite3
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table
cursor = connection.cursor()

## Query to create table
table_info = """
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""

## Create table in sqlite3
cursor.execute(table_info)

## Insert more records
cursor.execute('''Insert into STUDENT values('Aditya', 'AI Engineer', 'A', 90) ''')
cursor.execute('''Insert into STUDENT values('Krish', 'Data Science', 'B', 98) ''')
cursor.execute('''Insert into STUDENT values('Mukesh', 'Devops', 'A', 86) ''')
cursor.execute('''Insert into STUDENT values('Jack', 'Devops', 'B', 70) ''')
cursor.execute('''Insert into STUDENT values('Rohan', 'SWE', 'A', 76) ''')


## Display all the records
print("The inserted Records are:")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit changes in Database
connection.commit()
connection.close()