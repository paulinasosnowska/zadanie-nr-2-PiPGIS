# -*- coding: utf-8 -*-

class Pilkarze:
    def __init__(self, imie, nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko
    def get_imie(self):
        return self.__imie
    def set_imie(self,imie):
        self.__imie=imie
    def get_nazwisko(self):
        return self.__nazwisko
    def set_nazwisko(self,nazwisko):
        self.__nazwisko=nazwisko
    def oni(self):
        print "imie= " +self.imie+" nazwisko= " +self.nazwisko

class Hiszpancsy(Pilkarze):
    def __init__(self, imie, nazwisko, Hiszpania):
        Pilkarze.__init__(self, imie, nazwisko)
        self.Hiszpania=Hiszpania
    def info(self):
        print "Imię i nazwisko piłkarza: "+self.imie+self.nazwisko+" z hiszpańskiego klubu: " +self.Hiszpania

class Angielscy(Pilkarze):
    def __init__(self, imie, nazwisko, Anglia):
        Pilkarze.__init__(self, imie, nazwisko)
        self.Anglia=Anglia
    def info(self):
        print "Imię i nazwisko piłkarza: "+self.imie+self.nazwisko+" z angielskiego klubu: " +self.Anglia
        
class Niemieccy(Pilkarze):
    def __init__(self, imie, nazwisko, Niemiecy):
        Pilkarze.__init__(self, imie, nazwisko)
        self.Niemiecy=Niemiecy
    def info(self):
        print "Imię i nazwisko piłkarza: "+self.imie+self.nazwisko+" z niemieckiego klubu: " +self.Niemiecy
        
class Polscy(Pilkarze):
    def __init__(self, imie, nazwisko, Polska):
        Pilkarze.__init__(self, imie, nazwisko)
        self.Polska=Polska
    def info(self):
        print "Imię i nazwisko piłkarza: "+self.imie+self.nazwisko+" z polskiego klubu: " +self.Polska

class Wszyscy(Niemieccy, Polscy):
    def __init__(self, imie, nazwisko, Niemiecy, Polska):
        Pilkarze.__init__(self, imie, nazwisko)
        Niemieccy.__init__(self, imie, nazwisko, Niemiecy)
        Polscy.__init__(self, imie, nazwisko, Polska)
    def info2(self):
        print "Najlepszy piłkarz : "+self.imie+ self.nazwisko + "były klub: " +self.Polska + "obecny klub: " + self.Niemiecy 

David = Pilkarze("imię piłkarza","nazwisko piłkarza")
David.oni()
Iker = Hiszpancsy("Iker Casillas ", "Fernández", "Real Madryt")
Iker.info()
Steven = Angielscy("Steven ", "Gerrard", "Liverpool")
Steven.info()
Thomas = Niemieccy("Thomas ", "Müller", "Bayernie Monachium")
Thomas.info()
Sebastian = Polscy("Sebastian ", "Mila", "Śląsk Wrocław")
Sebastian.info()
Najlepsi = Wszyscy("Robert ", "Lewandowski ", "Bayernie Monachium", "Lech Poznań ")
Najlepsi.info2()