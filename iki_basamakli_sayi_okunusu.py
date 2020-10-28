birler = ["","Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz",""]
onlar = ["","On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan",""]

def sayıokuma(sayı):
    birinci = sayı % 10
    ikinci = sayı // 10

    return onlar[ikinci] + "" + birler[birinci]


sayı = int(input("Sayı Giriniz:"))

print(sayıokuma(sayı))