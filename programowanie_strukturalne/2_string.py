tekst = "Anna, Paweł, juLiA"
lista = tekst.split(", ")

print(tekst)
print(lista)
print(type(lista))
imie1 = lista[0]
print(imie1)

imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie1.lower()
print(imieMale)

#sprawdzenie zawartosci
print ("\nPodaj swoje nazwisko: ",end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc)

text1="\nJulia\n"
text2 = "Nowak"
print(text1 + text2)

text1 = text1.rstrip()
print(text1 +" " + text2)

text = "%s, java i %s" % ("PHP" , "Python")
print(text)

new = text.replace("PHP", "C#")
print (new)

#wypisanie danych
rok = 2019
miesiac = "kwiecień"
dzien = 27
print("\nData: ",end="")
print(dzien,miesiac,rok,sep="-")
