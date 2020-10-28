def mükemmelsayımı(sayı):

    tam_bolen = 0

    for i in range(1, sayı):
        if (sayı % i == 0):
            tam_bolen += i
    return tam_bolen == sayı

for i in range(1,1001):
    if(mükemmelsayımı(i)):
        print("Mükemmel Sayı:", i)


