import os

# os.rename('file testing', 'file testing_baru')

if os.path.isfile('file testing_baru') == True:
    print("Ada filenya nih masbro")
else:
    print("file tidak ditemukan masbro")