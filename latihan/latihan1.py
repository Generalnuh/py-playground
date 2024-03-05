todo_list = [
    "Belajar python",
    "Belajar php",
    "Belajar Java",
    "Belajar Laravel",
    "Belajar Django",
]

# menghapus index ke-2
del todo_list[2]
print(todo_list)
for todo in todo_list:
    print("saya akan belajar:")
    print("-", todo)

# Mengurutkan angka
angka = [1,5,3,7,6,4,2]
angka.sort()
print("Mengurutkan angka menggunakan short()" , angka)

# Membalikkan list
angka.reverse()
print("Membalikkan list menggunakan reverse()" , angka)

# Menghapus indeks terakhir
angka.pop()
print(angka)
print("Menghapus indeks terakhir pop()" , angka)

# Memotong list

count = [1,2,3,4,5,6,7,8,9]
print (count [2: 6])

list_satu = [10,45,22,54,67]

print(len(list_satu))
print(min(list_satu))
print(max(list_satu))
print(f"Total dari variable list_satu: {sum(list_satu)}")

list_satu.insert(3, 20)

for list in list_satu:
    print(list)