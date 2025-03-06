import sqlite3

# Connect to SQLite database (creates 'student.db' if it doesn't exist)
connection = sqlite3.connect('student.db')
cursor = connection.cursor() 

# Create table if it does not exist
table_info = """ 
CREATE TABLE IF NOT EXISTS student (
    NAME VARCHAR(25), 
    CLASS VARCHAR(25), 
    SECTION VARCHAR(25)
) 
"""
cursor.execute(table_info)

# Insert data into the table
students = [
    ('Karim', 'AI', 'A'),
    ('Emad', 'ML', 'A'),
    ('Alback', 'DL', 'C'),
    ('Mesho', 'GenAI', 'B')  # Fixed spelling: "GEnai" → "GenAI"
]

cursor.executemany("INSERT INTO student VALUES (?, ?, ?)", students)

# Commit the changes
connection.commit()

# Retrieve and display the data
print("The data inserted is:")
data = cursor.execute("SELECT * FROM student")
for row in data:
    print(row)

# Close the connection
connection.close()
