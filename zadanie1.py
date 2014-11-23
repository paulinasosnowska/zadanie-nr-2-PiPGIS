# -*- coding: utf-8 -*-

#zdefiniowanie dwoch plikow oraz ich otworzenie
tekst = open("zadanie1.txt","r") 
tekst2=open("statystyki.txt","a")

#wyswietlenie analizowanego tekstu
znaki = tekst.read()
print znaki

#wyswietlenie poszczegolnych slow w formie list
lista=[]
wyrazy=znaki.split(" ")

slownik = dict( zip( wyrazy, wyrazy ) )

#policzenie poszczegolnych slow
for slowo in wyrazy:
    slownik[slowo] = wyrazy.count(slowo)
       
wystapienia_slow = [key for [key, value] in slownik.items()]
ilosc_wystapien = [value for [key, value] in slownik.items()]

wynik = dict( zip( wystapienia_slow, ilosc_wystapien ) )

print wynik

#parametry pliku tekstowego
tekst2.writelines("Słowo wystąpiło nastepującą ilość razy:\n");
tekst2.writelines("\n");
tekst2.writelines(str(wynik));

print "Wynik analizy w pliku statystyki."
tekst.close()
tekst2.close()