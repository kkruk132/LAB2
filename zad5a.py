#Zad 5 a


#Otwieranie pliku blokiem with i wydrukowanie wyników każdej linii w pliku
with open("notowania_gieldowe.txt", "r") as plik:
 for linia in plik:
    print(linia)
