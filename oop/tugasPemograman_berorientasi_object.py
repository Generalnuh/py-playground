"""
Nama : Muhammad Nuh
NIM  : 220504027
Unit : 01/2022
Contoh program OOP menggunakan bahasa python
"""
class Login:
    def __init__(self):
        self.nama = ""
        self.password = ""

    def proses_login(self, nama, password):
        self.nama = nama
        self.password = password

    def cek_login(self):
        if self.nama == "Muhammad Nuh" and self.password == "123":
            return True
        else:
            return False

# Penggunaan
pengguna = Login()
pengguna.proses_login("Muhammad Nuh", "123")
if pengguna.cek_login():
    print("Login berhasil")
else:
    print("Login gagal")
    