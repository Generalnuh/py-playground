#  Contoh dari saya
import datetime
import time

sekarang = datetime.datetime.now()

tanggal = sekarang.date()
waktu = sekarang.time()

# print('hari : ', tanggal.day)
# print('Bulan : ', tanggal.month)
# print('Tahun : ', tanggal.year)
# print('jam : ', waktu.hour)
# print('Menit : ', waktu.second)
# print('Detik : ', waktu.second )
print(f"Sekarang jam: {waktu.hour}:{waktu.minute}:{waktu.second}")
print(f"Sekarang tanggal: {tanggal.day}/{tanggal.month}/{tanggal.year}")