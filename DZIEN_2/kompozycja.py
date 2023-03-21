"""
przykład na kompozycję klas
"""

class Adres:
    def __init__(self,ulica,miasto,kod,kraj):
        self.ulica = ulica
        self.miasto = miasto
        self.kod = kod
        self.kraj = kraj

class Osoba:
    def __init__(self,imie,nazwisko,adres):
        self.imie = imie
        self.nazwisko = nazwisko
        self.adres = adres

class Pracownik:
    def __init__(self,imie,nazwisko,adres,id_prac):
        self.id_prac = id_prac
        self.person = Osoba(imie,nazwisko,adres)

adr = Adres("Czerwcowa 45","Rzeszów","28-999","Polska")
prac = Pracownik("Jan","Nowak",adr,343434)

print(prac.person.imie,prac.person.nazwisko)
print(prac.person.adres.miasto)
print(prac.id_prac)





