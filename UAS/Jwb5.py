import mysql.connector as conn

mysql = conn.connect(
    host = "localhost",
    port = 23306,
    user = "root",
    password ="p455w0rd",
    database =""
)
if mysql.is_connected():
    print("hai restu, kamu berhasil connect ke database")
    
    
cursor = db.cursor()
cursor.execute("CREATE DATABASE BAHASA_PEMPROGRAMAN")

print("Database berhasil dibuat!")
	cursor = db.cursor()
sql = """CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  address Varchar(255)
)
"""
cursor.execute(sql)

print("Tabel customers berhasil dibuat!")
cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("wisnu", "ngawi")
cursor.execute(sql, val)

db.commit()

print("{} data ditambahkan".format(cursor.rowcount))
cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = [
  ("azam", "Tangerang"),
  ("syifa", "Surabaya"),
  ("hasna", "Bandung"),
  ("hasan", "Jakarta")
]

for val in values:
  cursor.execute(sql, val)
  db.commit()

print("{} data ditambahkan".format(len(values)))
