print("""
*************************
Çift Sayılar
*************************
""")
liste = list()

for i in range(1,101):
    if(i % 2 == 0):
        liste.append(i)
    else:
        continue
print(liste)