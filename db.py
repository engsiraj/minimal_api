import sqlite3

conn = sqlite3.connect("todo.sqlite")

cursor = conn.cursor()
query = ''' CREATE TABLE Todo(
 id integer PRIMARY KEY,
 title text NOT NULL,
 task text NOT NULL
)'''

cursor.execute(query)
