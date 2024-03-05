# Contoh program
for i in range(1, 100):
    if i == 65:
        print("Berhenti di nomor ke-{}" .format(i))
        print("dan dilanjutkan dinomor berikutnya")
        continue
    elif i == 70:
        print("program berhenti")
        break
    print(i)