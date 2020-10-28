print("""
**************************
ATM Programı

İşlemler:

1- Bakiye Sorgulama

2- Para Çekme

3- Para Yatırma

Çıkmak İçin X'e Basınız.
***************************
""")

bakiye = 5000

while True:
    işlem = input("İşlem Giriniz:")

    if(işlem == "X"):
        print("İşleminiz Sonlandı.")
        break
    elif(işlem == "1" ):
        print("Bakiyeniz {}'dir.".format(bakiye))
    elif(işlem == "2"):
        miktar = int(input("Çekmek İstediğiniz Miktarı Giriniz:"))
        if(bakiye - miktar < 0):
            print("Böyle Bir İşlem Gerçekleştiremezsiniz.")
            continue
        bakiye -= miktar
        print("{}t Para Çekme İşlemi Gerçekleştirildi. ".format(miktar))
    elif(işlem == "3"):
        miktar = int(input("Yatırmak İstediğiniz Miktarı Giriniz:"))
        bakiye += miktar
        print("{}t Para Yatırma İşlemi Gerçekleşti. ".format(miktar))

    else:
        print("Geçersiz İşlem.")