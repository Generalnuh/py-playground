import os
# Membuat folder
# os.mkdir("taman-bermain-pyku")

print(os.getcwd()) # <= mengecek folder yang sedang aktif

# os.rmdir('taman-bermain-pyku') # <= menghapus folder

# Mengecek ada tidak nya suatu folder
if os.path.isdir('crot') == True:
    print('ada masbro')
else:
    print('gaada masbro')

# untuk mengecek apa aja isi modul os
print(dir(os))
