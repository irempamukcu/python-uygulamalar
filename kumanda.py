import random
import time

class Kumanda():

    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["TRT"] , kanal = "TRT"):

        self.tv_durum = tv_durum

        self.tv_ses = tv_ses

        self.kanal_listesi = kanal_listesi

        self.kanal = kanal

    def tv_aç(self):
        if(self.tv_durum == "Açık"):
            print("Tv Açık.")
        else:
            print("Tv Açılıyor.")
        self.tv_durum = "Açık"

    def tv_kapat(self):
        if(self.tv_durum == "Kapalı"):
            print("Tv Kapalı.")
        else:
            print("Tv Kapanıyor.")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):

        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Artır: '>'\nÇıkış : çıkış")

            if(cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
            elif(cevap == ">"):
                if(self.tv_ses != 100):

                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)
            else:
                print("Ses Güncellendi.",self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal Ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal Eklendi")

    def rastgele_kanal(self):

        rastgele = random.randint(0,len(self.kanal_listesi)-1)


        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):


        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu Anki Kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda = Kumanda()

print("""
Televizyon Uygulaması

a.Tv Aç
b.Tv Kapat
c.Ses Ayarları
d.Kanal Ekle
e.Kanal Sayısı Öğrenme
f.Rastgele Kanala Geçme
g.Televizyon Bilgileri

Çıkmak için x'e basın.


""")


while True:

    işlem = input("İşlem Giriniz:")

    if(işlem == "x"):
        print("Program Sonlandırıldı.")
        break

    elif(işlem == "a"):
        kumanda.tv_aç()

    elif(işlem == "b"):
        kumanda.tv_kapat()

    elif(işlem == "c"):
        kumanda.ses_ayarları()

    elif(işlem == "d"):
        kanal_isimleri = input("Kanal İsimlerini',' ile Ayırarak Giriniz:")
        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif(işlem == "e"):
        print("Kanal Sayısı:",len(kumanda))

    elif(işlem == "f"):
        kumanda.rastgele_kanal()

    elif(işlem == "g"):
        print(kumanda)
    else:
        print("Geçersiz İşlem.")