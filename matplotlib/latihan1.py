import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Membuat plot
plt.plot(x, y)

# Menampilkan plot
plt.show()

plt.plot(x, y)
plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')
plt.title('Grafik Garis')
plt.show()
