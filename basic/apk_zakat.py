# Variabel berbentuk array
nama = []
gaji = []
emas = []
zakat = []
pertahun = []
perbulan = []
nisab = []
data = 1

def main():
    global data
    print('+-----------------------------------------------+')
    print('|         Menghitung Zakat Penghasilan          |')
    print('|      menurut pendapatan kasar (brutto)        |')
    print('|                                               |')
    print('+-----------------------------------------------+')
    data = int(input('Masukkan banyak data yang ingin diinputkan: '))
    print('==========================================')
    return data

main()

# Looping untuk menghitung jumlah data yang ingin diinput
def input_data(data):
    for i in range(data):
        nama.append(input('Masukkan nama: '))
        emas.append(int(input('Masukkan harga emas: ')))
        gaji.append(int(input('Berapa penghasilan/bulan: ')))
        print('')

# Formula penghitungan zakat dengan acuan 2.5% nisab emas
def hitung_zakat(data):
    for i in range(data):
        pertahun.append(12 * gaji[i])
        zakat.append(0.025 * pertahun[i])
        nisab.append(85 * emas[i])
        perbulan.append(zakat[i] / 12)

# Output print (user interface)
def print_output(data):
    for i in range(data):
        print('')
        print('----------------------------------------')
        print('      Zakat Penghasilan (Brutto)', nama[i])
        print('----------------------------------------')
        print('Nama                         :', nama[i])
        print('Harga 1 gram emas            :','Rp.', emas[i])
        print('Penghasilan per bulan        :','Rp.', gaji[i])
        print('Penghasilan per tahun        :','Rp.', pertahun[i])
        print('Harga nisab (85 gram emas)  :','Rp.', nisab[i])
        print('Zakat penghasilan            :','2.5% x', pertahun[i],'=','Rp.', zakat[i])
        if pertahun[i] >= nisab[i]: # Decision ya atau tidak
            print('Keterangan                   : WAJIB Zakat Rp.', zakat[i], '/tahun')
            print('                               atau Rp. ', perbulan[i], '/bulan')
            print('')
        else:
            print('Keterangan                   : Anda BELUM WAJIB Zakat')
            print('')

# Memanggil fungsi-fungsi yang telah didefinisikan
def main_process(data):
    input_data(data)
    hitung_zakat(data)
    print_output(data)

main_process(data) # Proses pemanggilan fungsi
