def üçgenbulma():

    liste1 = list()
    for i in range(1,101):
        for j in range(1,101):
            c = (i ** 2 + j ** 2 ) ** 0.5

            if(c == int(c)):
                liste1.append((i,j,c))

    return liste1

for i in üçgenbulma():
    print(i)