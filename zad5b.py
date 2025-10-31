#Zad 5 b


#Dopisywanie na końcu pliku nowej spółki ALR, 113
with open("notowania_gieldowe.txt", "a") as plik:
 plik.write("\nALR, 113")
#Odczytywanie pliku
with open("notowania_gieldowe.txt", "r") as plik:
 for linia in plik:
    print(linia)
