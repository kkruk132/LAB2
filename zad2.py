#Zad 2


#zmienne x,y,z podawane przez użytkownika
x = float(input("podaj zmienną x:"))
y = float(input("podaj zmienną y:"))
z = float(input("podaj zmienną z:"))


#pętla if porządkująca te zmienne i drukująca wynik od najmniejszej do największej wartości
if x >= y and x>= z:
    if y >= z:
        print(z, y, x)
    else:
        print(y, z, x)
elif y >=x and y >= z:
    if x >= z:
        print(z, x, y)
    else:
        print(x, z, y)
elif z >= x and z >= y:
    if x >= y:
        print(y, x, z)
    else:
        print(x, y, z)