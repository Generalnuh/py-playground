# Default argumen
def sapaan(nama="nuh"):
    print(nama)

sapaan("wahyu")

# Argumen list

def hitung(*angka):
    total = 0
    for hasil in angka:
        total = total + hasil
    print(f"Total pertambahan {angka} = {total}")

hitung(10, 1, 2)
