import sqlite3

DB_NAME = 'school.db'

def connect_db():
    return sqlite3.connect(DB_NAME)

def add_student(name, age, grade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
        (name, age, grade)
    )
    conn.commit()
    conn.close()

def read_students():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM students')
    data = cur.fetchall()
    conn.close()
    return data

# Example usage
name = input("Enter student name: ")
age = int(input("Enter student age: "))
grade = input("Enter student grade: ")

add_student(name, age, grade)
print(read_students())
