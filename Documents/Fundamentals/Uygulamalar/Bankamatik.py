import os 
def Menu():
    menuMetin = """
    1-Para Çekme
    2-Para Gönderme
    3-Bakiye Görüntüleme
    4-Para Yatırma
    5-Hesap Döküm
    6-Hesap Açma
    7-Çıkış
    """
    islem = input(menuMetin)

hesapAdres = os.path.join("Documents","Fundamentals","Uygulamalar","hesap.csv")
logAdres = os.path.join("Documents","Fundamentals","Uygulamalar","log.csv") 
hataAdres = os.path.join("Documents","Fundamentals","Uygulamalar","hata.csv") 



def dosyaOku(adres):
    mod = "r"
    if os.path.exists(adres):
        mod = "r+"
    else:
        mod = "w+"
    return open(adres,mod)

def dosyaKaydet(dosya,liste):
    dosya.seek(0)
    dosya.truncate()
    dosya.writelines(liste)
    dosya.flush()


def hesapAcma():
    numaralistesi = [ int(item.split(";")[0]) for item in hesapList]
    hesapNo = max(numaralistesi)+1
    isim = input("Hesap İsmi Giriniz:")
    hesapList.append(";".join([str(hesapNo),isim,"0"])+"\n")

def hesapListele():
    for item in hesapList:
        satir = item.split(";")
        print(f"{satir[0]}-{satir[1]}-{satir[2]}",end="")

def paraCekme(hesapId):
    hesap = []
    hesapindex = -1
    for i in range(len(hesapList)):
        satir = hesapList[i].replace("\n","").split(";")
        if satir[0] == hesapId:
            hesapindex = i
            hesap = satir
    tutar = input("Çekmek istediğiniz tutarı giriniz:")
    if tutar and tutar.isdigit():
        tutar = int(tutar)
    if int(hesap[2]) > tutar:
        hesap[2] = str(int(hesap[2]) - tutar)
        hesapList[hesapindex] = ";".join(hesap)+"\n"
    else:
        print("Hesap Müsait Değil")
    return True




hesapDosya = dosyaOku(hesapAdres)
hesapList = hesapDosya.readlines()
paraCekme("1")
hesapListele()
# hesapAcma()
# dosyaKaydet(hesapDosya, hesapList)
