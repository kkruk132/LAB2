#Zad 4 b


#zmienna gol pobierająca od użytkownika liczbę strzelonych bramek
gol = float(input("Podaj całkowitą liczbę bramek:"))
#zmienna bonus reprezentująca wszystkie punkty bonusowe
bonus = 10 * gol
#pętla if obliczająca punkty i drukująca wynik
if gol >= 5:
    bonus = bonus + 5
    print("Drużyna posiada następująca liczbę punktów:",bonus)
    print("\nLiczba goli wynosi:",gol)
elif gol >=10:
    bonus = bonus + 10
    print("Drużyna posiada następująca liczbę punktów:",bonus)
    print("\nLiczba goli wynosi:",gol)
else:
    print("Drużyna posiada następująca liczbę punktów:",bonus)
    print("\nLiczba goli wynosi:",gol)