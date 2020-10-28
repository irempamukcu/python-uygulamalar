class Hayvanlar():
    def __init__(self,çıkardığı_ses,en_önemli_özellik,renk,yediği_şey,cinsi,bilimsel_ismi):
        self.çıkardığı_ses = çıkardığı_ses
        self.en_önemli_özellik = en_önemli_özellik
        self.renk = renk
        self.yediği_şey = yediği_şey
        self.cinsi = cinsi
        self.bilimsel_ismi = bilimsel_ismi
class Köpek(Hayvanlar):
    def __init__(self,çıkardığı_ses,en_önemli_özellik,renk,yediği_şey,cinsi,bilimsel_ismi,koku_alma):
        super().__init__(çıkardığı_ses,en_önemli_özellik,renk,yediği_şey,cinsi,bilimsel_ismi)
        print("int fonksiyonu")
        self.koku_alma = koku_alma

    def bilgilerigöster(self):
        print("Bilgiler:\nÇıkardığı Ses:{}\nEn Önemli Özelliği:{}\nRengi:{}\nYediği Şey:{}\nCinsi{}\nBilimsel İsmi{}\nKoku Alma Oranı{}".format(self.çıkardığı_ses,self.en_önemli_özellik,self.renk,self.yediği_şey,self.cinsi,self.bilimsel_ismi,self.koku_alma))

class Kuş(Hayvanlar):
    def __init__(self,çıkardığı_ses,en_önemli_özellik,renk,yediği_şey,cinsi,bilimsel_ismi,gaga_şekli):
        super().__init__(çıkardığı_ses,en_önemli_özellik,renk,yediği_şey,cinsi,bilimsel_ismi)
        print("int fonksiyonu")
        self.gaga_şekli = gaga_şekli
    def bilgilerigöster(self):
        print("Bilgiler:\nÇıkardığı Ses:{}\nEn Önemli Özelliği:{}\nRengi:{}\nYediği Şey:{}\nCinsi{}\nBilimsel İsmi{}\nGaga Şekli{}".format(self.çıkardığı_ses,self.en_önemli_özellik,self.renk,self.yediği_şey,self.cinsi,self.bilimsel_ismi,self.gaga_şekli))

class At(Hayvanlar):
    def __init__(self,çıkardığı_ses,en_önemli_özellik,renk,yediği_şey,cinsi,bilimsel_ismi,boyut):
        super().__init__(çıkardığı_ses,en_önemli_özellik,renk,yediği_şey,cinsi,bilimsel_ismi)
        print("int fonksiyonu")
        self.boyut = boyut
    def bilgilerigöster(self):
        print("Bilgiler:\nÇıkardığı Ses:{}\nEn Önemli Özelliği:{}\nRengi:{}\nYediği Şey:{}\nCinsi{}\nBilimsel İsmi{}\nBoyut{}".format(self.çıkardığı_ses,self.en_önemli_özellik,self.renk,self.yediği_şey,self.cinsi,self.bilimsel_ismi,self.boyut))


bobby = Köpek("Hav","Sadık","Alacalı","Et","Dalmaçyalı","Canis","Çok İyi")
nane = Kuş("Cik","Aynada Hoplaması","Sarı-Yeşil","Mama","Muhabbet Kuşu","Avem","Yuvarlak")
doru = At("Yihaha","Koşması","Siyah","Küp Şeker","Beygir","Ferus","Çok Büyük")

bobby.bilgilerigöster()
nane.bilgilerigöster()
doru.bilgilerigöster()

