list_nomor = []

for i in range(1, 111):
    if i == 9:
        print(f"berhenti di angka ke-{i}")
        break
    print(i)

# Contoh program
input_data = int(input("Mau input berapa data: "))
nama = []
usia = []

for i in range(0, input_data):
    print(f"Data ke-{i}")
    input_nama = input("Masukkan nama: ")
    input_usia = int(input("Masukkan usia: "))

    nama.append(input_nama)
    usia.append(input_usia)

for i in range(0, len(nama)):
    data_nama = nama[i]
    data_usia = usia[i]

    print(f"Nama kamu, {data_nama} usia kamu, {data_usia} tahun")
