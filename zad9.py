#Zad 9


#zmienna pobierająca tekst do zamienienia od użytkownika
text = input(str("Podaj tekst do zamienienia dużych liter na małe i odwrotnie:"))

#zamiana używając swapcase()
text = text.swapcase()
print(text)