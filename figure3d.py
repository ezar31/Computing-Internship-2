from math import pi
from math import sqrt

class Kubus:
    # Initializer / Instance attributes
    def __init__(self, sisi):
        self.sisi = sisi
        
    # Attribute
    jumlah_sisi = 6

    # Method
    def hitung_luas(self):
        luas = self.jumlah_sisi*self.sisi**2
        print("Luas : {}".format(luas))

    def hitung_volume(self):
        volume = self.sisi**3
        print("Volume : {}".format(volume))


class Balok:
    # Initializer / Instance attributes
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        
    # Attribute
    jumlah_sisi = 6

    # Method
    def hitung_luas(self):
        luas = 2*(self.panjang*self.lebar+self.panjang*self.tinggi+self.lebar*self.tinggi)
        print("Luas : {}".format(luas))
        
    def hitung_volume(self):
        volume = self.panjang*self.lebar*self.tinggi
        print("Volume : {}".format(volume))

class Tabung:
    # Initializer / Instance attributes
    def __init__(self, jari, tinggi):
        self.jari = jari
        self.tinggi = tinggi
        
    # Attribute
    jumlah_sisi = 3

    # Method
    def hitung_luas(self):
        luas = (2*pi*self.jari**2) + (pi*2*self.jari*self.tinggi)
        print("Luas : {}".format(luas))
        
    def hitung_volume(self):
        volume = (pi*self.jari**2)*self.tinggi
        print("Volume : {}".format(volume))

class Kerucut:
    # Initializer / Instance attributes
    def __init__(self, jari, tinggi):
        self.jari = jari
        self.tinggi = tinggi
        
    # Attribute
    jumlah_sisi = 2

    # Method
    def hitung_luas(self):
        s = sqrt(self.jari**2 + self.tinggi**2)
        luas = (pi*self.jari*(self.jari+s))
        print("Luas : {}".format(luas))
        
    def hitung_volume(self):
        volume = ((pi*self.jari*self.jari*self.tinggi)/3)
        print("Volume : {}".format(volume))