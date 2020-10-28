giriş_hakkı = 3
sys_kullanıcı_adı = "İrem"
sys_parola = 1312
while True:
    kullanıcı_adı = input("Kullanıcı Adı:")
    parola = int(input("Parola:"))
    if(kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola):
        print("Hatalı Parola...")
        giriş_hakkı -= 1
    elif(kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Hatalı Kullanıcı Adı...")
        giriş_hakkı -= 1
    elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Hatalı Kullanıcı Adı Ve Parola...")
        giriş_hakkı -= 1
    else:
        print("Giriş Başarılı.")
        break

    if(giriş_hakkı == 0):
        print("Giriş Hakkınız Bitti, Sonra Tekrar Deneyin.")
        break
