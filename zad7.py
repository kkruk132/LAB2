# zad 7

#zmienna Hasło
Hasło = 'pk47!jy0893'
DlugoscHasla = len(Hasło)

#sprawdzanie hasła pętlą if i "!" in hasło i drukowanie wyników
if DlugoscHasla >= 11 and "!" in Hasło:
    print("Hasło jest poprawne")
else:
    print("Hasło jest nie poprawne")