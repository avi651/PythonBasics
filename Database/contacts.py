import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name,phone,email) VALUES('Tim',736374,'time@email.com')")
db.execute("INSERT INTO contacts(name,phone,email) VALUES('Brain',1234,'brain@yemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("_" * 20)

db.close()
