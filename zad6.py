#zad 6


#Pobieranie literki od użytkownika
litera = input(str("Podaj literę:"))

#sprawdzenie litery i drukowanie wyników używając funkcji isupper i islower i pętli if
if litera.isupper():
    print("Litera jest duża")
elif litera.islower():
    print("Litera jest mała")
else:
    print("Litera jest niepoprawna")