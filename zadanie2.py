# -*- coding: utf-8 -*-

# wczytanie dostępnego menu
potrawy = open("menu.txt","r") 
dania = potrawy.read()
print "Dostępne potrawy:"
print dania


# zdefiniowanie poszczególnych dań
menu={}
with open("menu.txt","r") as potrawy:
    for line in potrawy:
        (key,val)=line.split()
        menu[key]=float(val)

# obliczenie kwoty do zapłaty z wliczonym napiwkiem
def zamowienie(zamowienie):
    wartosc=0
    for element in zamowienie:
        if element in menu:
            wartosc=wartosc+menu[element]
    return "Kwota do zapłaty wynosi: "+str(wartosc*1.15) + " zł"

# w [] należy wpisać wybraną potrawę z menu
print zamowienie(["frytki","zupa","sok"])



