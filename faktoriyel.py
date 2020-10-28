print("""
************************
Faktöriyel Bulma Programı

Çıkmak İçin X'e Basınız.

************************

""")

while True:
    sayı = input("Sayı:")
    if(sayı == "X" or sayı == "x"):
        print("Program Sonlandırılıyor...")
        break

    else:
        sayı = int(sayı)

        faktoriyel = 1

        for i in range(2,sayı+1):
            faktoriyel *= i
        print(faktoriyel)
