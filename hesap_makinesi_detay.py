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
            def faktöriyel():
                sayı = input("Sayı:")

                sayı = int(sayı)

                faktoriyel = 1

                for i in range(2, sayı + 1):
                    faktoriyel *= i
                print(faktoriyel)


            faktöriyel()

        elif(işlem == 7):
            sayı = int(input("Sayı:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            print(sayı ** 2)

        elif(işlem == 8):
            sayı = int(input("Sayı:"))
            print("Hesaplanıyor...")
            time.sleep(1)
            print(sayı ** 0.5)

        elif(işlem == 9):
            sayı = int(input("Sayı:"))
            if(sayı < 0):
                sayı *= -1
                print(sayı)
            else:
                print(sayı)




