import datetime
import time

waktu_sekarang = datetime.datetime.now()

tanggal = waktu_sekarang.date()
jam = waktu_sekarang.time()

print(f"Sekarang tanggal: {tanggal.day}/{tanggal.month}/{tanggal.year}")
print(f"Sekarang jam: {jam.hour}:{jam.minute}:{jam.second}")