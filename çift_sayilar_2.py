def çiftsayı(sayı):
    if(sayı % 2 == 0):
        return sayı
    else:
        raise ValueError

liste1 = [1,2,3,4,5,6]

for i in liste1:
    try:
        print(çiftsayı(i))
    except ValueError:
        continue