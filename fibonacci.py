print("""
*********************
Fibonacci Uygulaması
*********************

""")

while True:
    sayı = int(input("Sayı:"))

    if(sayı == 0):
        print("Bu sayıyı giremezsiniz.")
        break
    else:
        print(sayı)
        sayı += sayı
        aşama = int(input("Aşama:"))
        aşama -= 1
        if(aşama == 0):
            print(sayı)
            break
