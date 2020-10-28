liste = ["123","ekdf","löfefö344","3434345","56534654","5","a"]

for i in liste:
    try:
        print(int(i))
    except ValueError:
        continue

