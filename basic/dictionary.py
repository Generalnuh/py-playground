# Dictionary Contoh

info = {
    "nama" : "Muhammad Nuh",
    "nim" : 220504027,
    "prodi" : "Teknik Informatika",
    "Pacar" :{
        "utama" : "indah",
        "backup" : "adel"
    }
}

# Bisa juga menggunakan construct dict
warna = dict(favWarna = "hitam", minWarna = "orange")
print(warna["favWarna"])

iniAku = {
    "nama" : "Muhammad Nuh",
    "nim" : 220504027,
    "hobi" : ["gatau", "bermalas-malasan", "boros"],
    "cita-cita" : "Menjadi kamen rider",
    "pacar" : {
        "satu" : "Tidak ada",
        "dua" : "satupun tak de😚"
    }
}

print("Namaku  : %s" % iniAku["nama"])
print("Pacarku : %s" % iniAku["pacar"] ["dua"])

for key in iniAku:
    print(iniAku[key])

print("Daftar Pacar:")
for i in iniAku["pacar"]:
    print("-%s" % iniAku["pacar"][i])

# Mengubah item di dictionary
mySkill = {
    "utama" : "python",
    "languange" : ["php", "java", "kotlin"],
    "framework" : "Only Spring😎",
    "bosan" : "tak terhingga⁐"
}

mySkill["utama"] = ["Rust"]
# Menghapus
del mySkill["bosan"]

# Mengakses dan mencetak semua kunci dan nilainya
for key, value in mySkill.items():
    print(f"{key}: {value}")

# Mengakses dan mencetak semua bahasa pemrograman yang saya pelajari
print("\nBahasa pemrograman yang saya pelajari:")
for language in mySkill["languange"]:
    print(language)

# Mengakses dan mencetak semua karakter dalam framework
print("\nKarakter dalam framework yang saya kuasai:")
for char in mySkill["framework"]:
    print(char)

# Menghapus menggunakan methode pop()
skill = {
    "skill1" : "Burst damage",
    "skill2" : ["true damage", "ability", "turet gamempan"]
}
print(skill)

skill.pop("skill1")
print(skill)

# menambahkan item ke directory
user = {
    "nama" : "admin"
}

# Menambahkan password
user.update({"password" : "123"})
print(user)

# Mengopi dictionary
x = dict(username = "admin", machines = ["foo", "bar", "baz"])

y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(x)
print(y)