"""
przykład agregacji klas
"""

class Departament:
    def __init__(self,nazwa,pracownicy):
        self.nazwa = nazwa
        self.pracownicy = pracownicy

class Pracownik:
    def __init__(self, imie, nazwisko, departament):
        self.imie = imie
        self.nazwisko = nazwisko
        self.departament = departament

dep = Departament("Sprzedaż",[])
prac1 = Pracownik("Jan","Kot",dep)
prac2 = Pracownik("Olga","Nowak",dep)
dep.pracownicy.append(prac1)
dep.pracownicy.append(prac2)

print(dep.nazwa)
print(len(dep.pracownicy))
print(dep.pracownicy[0].imie,dep.pracownicy[0].nazwisko)
print(dep.pracownicy[1].imie,dep.pracownicy[1].nazwisko)
