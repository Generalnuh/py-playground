# modul mtk

import math

# konstanta
print('pi = ', math.pi)
print('e = ', math.e)

# factorial n!
for i in range(1, 11):
    print('%s! = %s' % (i, math.factorial(i)))

# pangkat
print('2 pangkat dari 12 = ', math.pow(2, 12))

# akar kuadrat
print('Akar kuadrat dari 10 = ', math.sqrt(10))

# Logaritma
print('log 8 = ', math.log(8))
print('log 8 basis 10 = ', math.log(8, 10))
print('log 8 basis 10 = ', math.log10(8))

# trigonometri
print('sin 90 derajat = ', math.sin(math.radians(90)))

print(dir(math))