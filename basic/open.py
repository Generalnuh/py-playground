objek_file = open('/mnt/DATA E/python/py-playground/img/gambar1.png', 'r+')

f = open('file testing', 'w')
f.write('Baris pertama\n')
f.write('Baris kedua\n')
f.write('baris ketiga ganteng -_-\n')
f.close()
# print('File tersebut berada di' . os.getcwd())

f = open('file testing', 'r')
print(f.read(25))

# perulangan
# 1
f = open('file testing', 'r')
for i in range(3):
    print(str(i) + ': ' + f.readline())

# 2
f = open('file testing', 'r')
for line in f.readlines():
    print("-%s" % line)

# 3
f = open('file testing', 'r')
a = ''
for char in f.read():
    a = a + char
print(a)

