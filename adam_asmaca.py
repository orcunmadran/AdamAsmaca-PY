from random import randint

adamCan = 3

kelimeler = ["bisiklet", "triatlon", "yüzme", "koşu"]
kelimeSayisi = len(kelimeler)
secilen = randint(0, kelimeSayisi-1)
secilenKelime = kelimeler[secilen]
print(secilenKelime)
dizilenKelime = []
for diz in kelimeler[secilen]:
    dizilenKelime.append("_")
print(dizilenKelime)

while adamCan > 0:
    girilenHarf = input("Bir harf giriniz: ")
    canKontrol = girilenHarf in secilenKelime
    if canKontrol == False:
        adamCan-=1
    i = 0
    for kontrol in secilenKelime:
        if secilenKelime[i] == girilenHarf:
            dizilenKelime[i] = girilenHarf
        i+=1
    print(dizilenKelime)
    print("Kalan can: "+ str(adamCan))
