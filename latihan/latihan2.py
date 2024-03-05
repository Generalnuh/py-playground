# Latihan ke dua

jumlah_elemen = 5

angka = []
sum = 0

for i in range(jumlah_elemen):
    value = eval(input("Masukkan angka: "))
    angka.append(value)
    sum += value

rata_rata = sum / jumlah_elemen
hitung = 0

for i in range(jumlah_elemen):
    if angka[i] > rata_rata:
        hitung +=1

print("Nilai rata-ratanya adalah: ", rata_rata)
print("Banyaknya angka di atas nilai rata-rata adalah: ", hitung)