import os 
from datetime import datetime


hesapAdres = os.path.join("Documents","Fundamentals","Uygulamalar","hesap.csv")
logAdres = os.path.join("Documents","Fundamentals","Uygulamalar","log.csv") 
hataAdres = os.path.join("Documents","Fundamentals","Uygulamalar","hata.csv") 

logDosya = open(logAdres,"a+")

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
    return True

def hesapListele():
    for item in hesapList:
        satir = item.split(";")
        print(f"{satir[0]}-{satir[1]}-{satir[2]}",end="")

def paraCekme(hesapId,tutar=0):
    hesap = []
    hesapindex = -1
    for i in range(len(hesapList)):
        satir = hesapList[i].replace("\n","").split(";")
        if satir[0] == hesapId:
            hesapindex = i
            hesap = satir
    if not tutar:
        tutar = input("Çekmek istediğiniz tutarı giriniz:")
        if tutar and tutar.isdigit():
            tutar = int(tutar)
        else:
            print("Yanlış Tutar Girişi")
            return False
    if int(hesap[2]) > tutar:
        hesap[2] = str(int(hesap[2]) - tutar)
        hesapList[hesapindex] = ";".join(hesap)+"\n"
        zaman=datetime.now()
        zamanBilgi = [zaman.day,zaman.month,zaman.year,zaman.hour,zaman.minute,zaman.second]
        zamanBilgi = list(map(str,zamanBilgi))
        # deneme = f"{';'.join(hesap)};{'.'.join(zamanBilgi)};PY"
        print(f"{';'.join(hesap)};{'.'.join(zamanBilgi)};PC",file=open(logAdres,"a+"),)
    else:
        return False
        print("Hesap Müsait Değil")
    return True




def paraYatırma(hesapId,tutar=0):
    hesap = []
    hesapindex = -1
    for i in range(len(hesapList)):
        satir = hesapList[i].replace("\n","").split(";")
        if satir[0] == hesapId:
            hesapindex = i
            hesap = satir
    if not tutar:
        tutar = input("Yatırmak istediğiniz tutarı giriniz:")
        if tutar and tutar.isdigit():
            tutar = int(tutar)
        else:
            print("Yanlış Tutar")
            return False
    hesap[2] = str(int(hesap[2]) + tutar)
    hesapList[hesapindex] = ";".join(hesap)+"\n"
    zaman=datetime.now()
    zamanBilgi = [zaman.day,zaman.month,zaman.year,zaman.hour,zaman.minute,zaman.second]
    zamanBilgi = list(map(str,zamanBilgi))
    print(f"{';'.join(hesap)};{'.'.join(zamanBilgi)};PY",file=open(logAdres,"a+"),)
    return True

def paraGonderme(hesapId1,hesapId2,tutar):
    if paraCekme(hesapId1,tutar):
        if paraYatırma(hesapId2,tutar):
            print("Para Gönderildi")
            zaman=datetime.now()
            zamanBilgi = [zaman.day,zaman.month,zaman.year,zaman.hour,zaman.minute,zaman.second]
            zamanBilgi = list(map(str,zamanBilgi))
            print(f"{hesapId1}=>{hesapId2}==={tutar};{'.'.join(zamanBilgi)};PG",file=open(logAdres,"a+"),)
            return True
        else:
            print("Hesaba Yatırılırken Sorun Oluştu")
            return False
    else:
        print("Hesaptan Para Çekilirken Sorun Oluştu")
        return False

hesapDosya = dosyaOku(hesapAdres)
hesapList = hesapDosya.readlines()

# hesapAcma()
# dosyaKaydet(hesapDosya, hesapList)
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
    anahtar =0
    while anahtar == 0:
        islem = input(menuMetin)
        if islem and islem.isdigit():
            if int(islem) in range(1,6):
                hesapListele()
                if islem == "1":
                    hesapId = input("Para Çekmek İstediğiniz HesapId giriniz:")
                    if paraCekme(hesapId):
                        print("Para Çekme İşlemi Başarılı")
                    else:
                        print("Bir Sorun Oluştur PÇ1")
                elif islem == "2":
                    hesapId1 = input("Para Çekmek İstediğiniz Hesabı Seçiniz:")
                    hesapId2 = input("Para Yatırmak İstediğiniz Hesabı Seçiniz:")
                    tutar = input("Tutarı Giriniz:")
                    tutar = int(tutar) if tutar and tutar.isdigit() else 0
                    if paraGonderme(hesapId1, hesapId2, tutar):
                        print("Para Gönderme Başarıyla Gönderildi")
                    else:
                        print("Para Gönderme Sorun Oluştu PG1")
                elif islem == "3":
                    pass # TODO bakiye görüntüleme fonksiyonu yazılacak
                elif islem == "4":
                    hesapId = input("Para Yatırmak İstediğiniz HesapId giriniz:")
                    if paraYatırma(hesapId):
                        print("Para Yatırma İşlemi Başarılı")
                    else:
                        print("Bir Sorun Oluştu PY1")          
                elif islem == "5":
                    pass # TODO hesap döküm fonksiyonu yazılacak
            elif islem == "6":
                if hesapAcma():
                    print("Hesabınız Açıldı")
                    hesapListele()
            elif islem == "7":
                anahtar = 1
    else:
        dosyaKaydet(hesapDosya, hesapList)
        print("Programdan Çıkılıyor")
    

Menu()
