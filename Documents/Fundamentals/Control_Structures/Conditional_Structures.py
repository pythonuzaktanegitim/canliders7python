# var1 = -1
# var2 = ""
# var3 = []
# if var1:
#     print("Dolu")
# else:
#     print("Boş")

# isim = input("İsim Giriniz:")
# if isim:
#     print("Merhaba",isim)
# else:
#     print("İsim Girilmedi")

""" Soru 1
iki açısı girilen bir üçgenin çeşidini ekrana yazdıran program
1. Açı : 45
2. Açı : 45
İkizkenar Üçgen
Dik Üçgen
"""
aci1 = input("1. Açıyı Giriniz:")
aci2 = input("2. Açıyı Giriniz:")
if aci1 and aci2:
    if aci1.isdigit() and aci2.isdigit():
        aci1 = int(aci1)
        aci2 = int(aci2)
        liste = [aci1,aci2,(180-(aci1+aci2))]
        if sum(liste) == 180:
            sonuc = set(liste) # type convertion
            if len(sonuc) == 1:
                print("Eşkenar Üçgen")
            elif len(sonuc) == 2:
                    print("İkizkenar Üçgen")
            else:
                print("Çeşitkenar Üçgen")
            if 90 in sonuc:
                print("Dik Üçgen")


a = 5
sonuc = "Tek" if a % 2 > 0 else "Çift"
