import mysql.connector

# Koneksi ke database
cnx = mysql.connector.connect(
    host="hostname",
    user="username",
    password="password",
    database="database_name"
)

cursor = cnx.cursor()

# Membuat tabel
create_table = """
CREATE TABLE lenovo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    akun VARCHAR(255)
)
"""
cursor.execute(create_table)

# Menambahkan data
add_user = "INSERT INTO lenovo (name, akun) VALUES (%s, %s)"
user_data = ("Restu Eka", "restueka27")
cursor.execute(add_user, user_data)
cnx.commit()

# Mengambil data
query = "SELECT * FROM users"
cursor.execute(query)

for (id, name, akun) in cursor:
    print("ID: {}, Name: {}, Akun: {}".format(id, name, akun))

# Menutup koneksi
cursor.close()
cnx.close()
