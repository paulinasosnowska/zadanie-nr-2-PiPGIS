# -*- coding: utf-8 -*-
from math import sqrt

class zespolone:
    def __init__(self, r, u):
        self.rzeczywista = r
        self.urojona = u 
    def get_r(self):
        return self._rzeczywista
    def set_r(self, r):
        self._rzeczywista=r
    def get_u(self):
        return self._urojona
    def set_u(self, u):
        self._urojona=u
    def dodawanie(self, zespolone):
        print "Wartość jest równa: " +str(self.rzeczywista+zespolone.rzeczywista) +str(self.urojona+zespolone.urojona)+'*i'
    def odejmowanie(self, zespolone):
        print "Różnica jest równa: " +str(self.rzeczywista-zespolone.rzeczywista)+str(self.urojona-zespolone.urojona)+'*i'
    def modul(self):
        print "Moduł wynosi: "+ str(sqrt((self.urojona)**2+(self.rzeczywista)**2))
    def wyswietlanie (self):
        print "Liczba w postaci r+ui: "+ str(self.rzeczywista)+" + "+str(self.urojona)+"i"
        
a=zespolone(3.0, -5.5)
b=zespolone(5.0, 3.0)
zespolone.dodawanie(a, b)
zespolone.odejmowanie(a,b) 
zespolone.modul(a)
zespolone.wyswietlanie(a)

    
