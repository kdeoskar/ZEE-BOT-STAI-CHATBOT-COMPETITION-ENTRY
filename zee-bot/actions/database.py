import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


#c.execute("""CREATE TABLE students (
#            idno integer, 
#            class integer,
#            section text,
#            first text,
#            last text
#            )""")

#c.execute('INSERT INTO students VALUES (13493, 12, "B", "Keshav", "Deoskar")')
#conn.commit()

'''
c.execute("SELECT * FROM students where idno = 13493")
r = c.fetchone()
cls = str(r[1])+r[2]
print(cls)

c.execute("SELECT class, section FROM students where idno = 13493")
r = c.fetchone()
cls = str(r[0])+r[1]
print(cls)
conn.close()

slot_value = int(input(":"))
c.execute("SELECT * FROM students WHERE idno = :idno", {"idno": slot_value})
r = c.fetchone()
print(r)
'''
c.execute("SELECT * FROM students")
r = c.fetchall()
print(r)
