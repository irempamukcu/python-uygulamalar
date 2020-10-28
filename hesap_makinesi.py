print("""
**************************
HESAP MAKİNESİ

İşlemler:

1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
5-Yüzdelik
6-Faktöriyel
7-Karesini Bulma
8-Karekök Bulma
9-Mutlak Değer
10-Logaritma


*************************

""")
import math
import time

işlem = input("İşlem Giriniz:")

while True:
    if (işlem == "x"):
        time.sleep(1)
        print("İşleminiz Sonlandırılıyor...")
        break
    else:
        işlem = int(işlem)

        if(işlem == 1):
            sayı = int(input("Sayı:"))
            sayı2 = int(input("Sayı2:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            print("{} + {} = {}".format(sayı, sayı2, sayı + sayı2))

        elif(işlem == 2):
            sayı = int(input("Sayı:"))
            sayı2 = int(input("Sayı2:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            print("{} - {} = {}".format(sayı, sayı2, sayı - sayı2))

        elif(işlem == 3):
            sayı = int(input("Sayı:"))
            sayı2 = int(input("Sayı2:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            print("{} * {} = {}".format(sayı, sayı2, sayı * sayı2))

        elif(işlem == 4):
            sayı = int(input("Sayı:"))
            sayı2 = int(input("Sayı2:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            print("{} / {} = {}".format(sayı, sayı2, sayı / sayı2))

        elif(işlem == 5):
            sayı = int(input("Sayı:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            print("%{} = {}".format(sayı, sayı / 100))

        elif(işlem == 6):
            sayı = int(input("Sayı:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            a = math.factorial(sayı)
            print(a)

        elif(işlem == 7):
            sayı = int(input("Sayı:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            print(sayı ** 2)

        elif(işlem == 8):
            sayı = int(input("Sayı:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            b = math.sqrt(sayı)
            print(b)

        elif(işlem == 9):
            sayı = int(input("Sayı:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            c = math.fabs(sayı)
            print(c)

        elif(işlem == 10):
            sayı = int(input("Sayı:"))
            sayı2 = int(input("Sayı2:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            d = math.log(sayı, sayı2)
            print(d)

        else:
            print("Hata. Geçerli Bir İşlem Giriniz.")



