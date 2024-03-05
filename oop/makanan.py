class makanan:
    __about = "Created by muhammadnuh"
    __menu = ""
    nama = ""
    def __init__(self, nama):
        self.nama = nama
    def get_about(self):
        print(self.__about)
        print("Yang dipilih : %s" % self.__menu)
    def set__food(self, isian):
        if isian == "sate":
            print("Sate kacang lebih enak dari sate padang emm...lapar deh")
        elif isian == "lontong":
            print("Lontong enak untuk sarapan dan makanan lebaran(hari raya)")
        elif isian == "nasi goreng":
            print("nasi ya bukan nazi(**hitler sfx)")
        else:
            print("No komen -_-")
        self.__menu = isian

m = makanan("siang")
m.set__food("nasi goreng")
m.get_about()

def tambah(panjang, lebar):
    total = panjang * lebar
    return total

masukkan_angka = tambah(10, 10)
print(masukkan_angka)