"""
print ("cdv")
print (2)
'''
komentarz
blokowy
'''

#potegowanie
potega = 2 ** 10
print (potega)

#pobieranie danych z klawiatury
imie = input("Podaj imie:")

print("Twoje imie z klawiatury: " + imie)

nazwisko = input("Podaj nazwisko:")

print("Twoje imie: " + imie + ", Twoje nazwisko " + nazwisko)
print("Podaj swoj wiek: ", end="")
wiek = input()
print(type(wiek))
print ("Twoj wiek: " + wiek)

wiek1=30
print(type(wiek1)) #int
print("Twoj wiek: " , wiek1)

#print("Twoj wiek: " + wiek1)

nazwisko = "Kowalski"
pierwszyZnak = nazwisko[0]
print(pierwszyZnak)

dlugosc = len(nazwisko)
print(dlugosc)

ostatniZnak = nazwisko[len(nazwisko)-1]
print(ostatniZnak)

ostatniZnak = nazwisko[-1]
print(ostatniZnak)
"""

x = "5"
print(type(x)) #str
x=int(x)
print(type(x)) #int
y=4
print(type(y)) #int

y = y/2
print(type(y))
print(y)
nazwisko = "Kowalski"
print(type(nazwisko))
print(nazwisko[0])
print(nazwisko[0:3])
print(nazwisko[0])
print(nazwisko[-2])
print(nazwisko[:-2:2])
