print("""
*******************
Toplama İşlemi:
*******************
""")
print("Çıkış İçin X'e Basınız")

toplam = 0

while True:
    sayı = input("Sayı Giriniz:")
    if(sayı == "x"):
        print("İşleminiz Sonlandı.")
        break
    else:

        sayı = int(sayı)
        toplam = toplam + sayı
        print("Toplam: {}".format(toplam ))


