class orang:
    def __init__(self, nama):
        self.nama = nama

    def nyapa(self):
        print('halou masbro, %s ' % self.nama)
        print('halou masbro, ' + self.nama)
        print(f"Halou masbro {self.nama}")
    
# manggil object^diatas
org = orang('kapibara')
org.nyapa()