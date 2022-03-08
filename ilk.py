import os
for i in range(1,10):
    os.mkdir(f"Takim{i}")
    dosya = open(os.path.join(os.getcwd(),f"Takim{i}","ilk.py"),"w")
    print(f"Merhaba Takım{i}",file=dosya)


    
"""
TEAM 1:
'Murat'
'Sinan'
'Gökçen'
'Ahmet'
TEAM 2:
'Joker2'
'Ümit'
'Yusuf'
'Aydın'
TEAM 3:
'Ayşegül'
'Yavuzelikucuk
'Osama'
'Tarık'
TEAM 4:
'Fatihyasin'
'Havva'
'Nazan'
'Joker1'
TEAM 5:
'Bilal'
'Eyyüp'
'Ferdi'
'Samet'
TEAM 6:
'Tayfun'
'Tarkan'
'Yasamin'
'Kasım'
TEAM 7:
'Yavuz'
'Cüneyt'
'Sedat'
'Selena'
TEAM 8:
'Yavuz'
'Damlanur'
'Cengiz'
'Enes'
TEAM 9:
'Batuhan'
'Kaan'
'Joker3'
'Kubilay'
"""