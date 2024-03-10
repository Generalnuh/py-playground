import datetime
import time

waktu_sekarang = datetime.datetime.now()

jam = waktu_sekarang.time()
hari = waktu_sekarang.date()

print(f"sekarang jam: {jam.hour}, menit: {jam.minute}, detik: {jam.second}")
print(f"Sekarang tanggal: {hari.day}, bulan: {hari.month}, tahun: {hari.year}")