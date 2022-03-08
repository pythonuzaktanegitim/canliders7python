liste = []


metin = """Gökçen Akgül
Kubilay Küçük
Selena Öztepe
cengiz mengenci
Cüneyt Özkurt
Bilal Benzer 
Kasım Doğruyol
Aydın Kapan
Tarık Furkan Kılıç
Yavuz Kemal Yaman
Ümit ALBAYRAK
Ayşegül Karataş
YAVUZ
Ferdi KILIÇ
Tarkan Aydın
nazan deniz
Tayfun Tepedibi 
Damlanur İlhan 
Eyyüp UZUN
Sinan YILDIRIM
Sedat Selam
Murat Can Aktosun
Yusuf Kılıç
Samet ATEŞ
kaan Çam
Havva İrem Avşar Göğercin
enes kaplan
OSAMA ELMOUSEL
Batuhan Emre
YASAMIN
ahmet
Joker1
Joker2
Joker3
fatihyasin
YavuzEliKucuk"""
liste = [item.split()[0] for item in  metin.split("\n")]
liste = list(map(lambda x:x.capitalize(),liste))
print(len(liste))
print(liste)
import random as rnd
ekipler=[]
def kontrol(secim):
    for eleman in secim:
        for item in ekipler:
            if eleman in item:
                return True
        else:
            return False
   
for i in range(9):
    secim = rnd.sample(liste,4)
    while kontrol(secim):
        secim = rnd.sample(liste, 4)
    else:
        ekipler.append(secim)


print(*ekipler,sep="\n")



























































































