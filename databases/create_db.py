import sqlite3

#connects to db / creates it if it doesn't exist
conn = sqlite3.connect('school.db')

#creates a cursor refrence : used to execute SQL commands
cursor = conn.cursor()

#creates a table for students
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
''')
# #inserts sample data into students table - sreate records to our table
# # ? placeholders to prevent SQL injection : prepared statements

# cursor.execute(
#     "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
#     ('Alice', 14, '9th Grade')

# )
cursor.execute(
    "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
    ('Jane', 14, '9th Grade')

)

# update record 
# cursor.execute(
#     "UPDATE students SET age = ? WHERE name = ?",
#     (15, 'Alice')
# )   
# delete record
 
cursor.execute(
     "DELETE FROM students WHERE name = ?",
     ('Alice',)
 )
# # rea ds all records from students table
cursor.execute(
               'SELECT * FROM students'
               )
rows = cursor.fetchall() #fetches all results from executed query
for row in rows:
    print(row)

conn.commit() #saves changes
conn.close() #closes connection