import pymysql

# Membuat koneksi ke database
db = pymysql.connect(host='localhost', user='root', password='', database='information_schema')

# Membuat objek cursor
cursor = db.cursor()

# Menjalankan perintah SQL untuk mendapatkan versi database
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()

# Mencetak versi database
print("Versi database: %s" % data[0])

# Menutup koneksi database
db.close()
