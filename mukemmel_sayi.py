print("""
***************************
Mükemmel Sayı
***************************
""")


sayı =int(input("Sayınızı Giriniz:"))

a = 0

for i in range(1,sayı):
    if(sayı % i == 0):
        a += i

if(a == sayı):
    print("Bu Bir Mükemmel Sayıdır.")
else:
    print("Bu Bir Mükemmel Sayı Değildir.")


