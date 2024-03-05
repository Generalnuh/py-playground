class Orang:
    def __init__(self, nama):
        self.nama = nama

    def katakanHai(self):
        print(f"hai nama saya {self.nama}, apakabar masbro!!!")

org = Orang("indah")
org.katakanHai()