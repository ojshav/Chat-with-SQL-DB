import sqlite3

conn = sqlite3.connect('my_database.db')

cursor = conn.cursor()

tabel_info = """
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT
)
"""

cursor.execute(tabel_info)

## Insert data into the table
cursor.execute("INSERT INTO student (name,age,gender) VALUES ('John',20,'Male')")
cursor.execute("INSERT INTO student (name,age,gender) VALUES ('Jane',21,'Female')")
cursor.execute("INSERT INTO student (name,age,gender) VALUES ('Jim',22,'Male')")
cursor.execute("INSERT INTO student (name,age,gender) VALUES ('Jill',23,'Female')")


## Display all data from the table
print("Displaying all data from the table")
for row in cursor.execute("SELECT * FROM student"):
    print(row)


conn.commit()

conn.close()
