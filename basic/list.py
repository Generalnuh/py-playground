# Tipe data list

teman_ku = ["jota", "suaib", "bedol", "tutul"]
print(f"daftar teman ku {teman_ku}")
print("Temanku sebanyak {}" . format(len(teman_ku)) + " orang")

for teman in teman_ku:
    print(teman) 


teman_ku.insert(3, "wabdul")
print("Nama teman-temanku: {}". format(teman_ku))

# Contoh program 
hobi = []
stop = False
i = 0

while(not stop):
    hobi_baru = input("Inputkan hobi ke-{}" .format(i))
    hobi.append(hobi_baru)
    i += 1
    tanya = input("Mau isi lagi? (y/t): ")
    if(tanya == "t"):
        stop = True
    
print("=" * 20)
print("Kamu memiliki {} hobi." .format(len(hobi)))
for hb in hobi:
    print("- {}" .format(hb))