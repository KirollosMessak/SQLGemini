import sqlite3
#connect to sqlite database
connection = sqlite3.connect('student.db')
cursor = connection.cursor() 
# a cursor is an object used to interact with the database. It allows you to execute SQL queries and retrieve results

table_info=""" 
CREATE table student (NAME VARCHAR (25), CLASS VARCHAR (25), 
SECTION VARCHAR (25)) 
"""
cursor.execute(table_info)

cursor.execute(''' Insert Into Student values ('karim' , 'AI', 'A')''')
cursor.execute(''' Insert Into Student values ('emad' , 'ML', 'A')''')
cursor.execute(''' Insert Into Student values ('Alback' , 'DL', 'C')''')
cursor.execute(''' Insert Into Student values ('Mesho' , 'GEnai', 'B')''')

print('the data inserted is')
data= cursor.execute(''' SELECT * FROM student''')
for row in data:
    print (row)