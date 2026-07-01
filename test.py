class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def suara(self):
        print(f"{self.nama} bisa bersuara")

harimau = Hewan("Maung", 12)
print(harimau.umur)
harimau.suara()

class Kucing(Hewan):
    pass

anggora = Kucing("Bonbon", 2)
anggora.suara()

class Anjing(Hewan):
    def gonggong(self):
        print("Suara hewan ini adalah gukguk")

wolly = Anjing("Wolly", 3)
wolly.suara()
wolly.gonggong()