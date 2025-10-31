#Zad 1


#podanie liczby punktów przez studenta
punkty = int(input("Podaj liczbę punktów: "))


#pętla if sprawdzająca liczbę punktów i drukująca odowiedni wynik
if punkty > 80 and punkty <= 100:
    print("Zdałeś w terminie 0 z liczbą punktów wynoszącą", punkty,"punktów")
elif punkty >= 50 and punkty <= 80:
    print("Nie zdałeś. Możesz poprawić. Twój wynik to",punkty,"punktów")
elif punkty <= 50:
    print("Nie zdałeś. Musisz poprawić. Twój wynik to",punkty,"punktów")
else:
    print("Podałeś niepoprawną liczbę punktów")