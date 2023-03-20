class Oprawa:
    def __init__(self, rodzaj, grubosc):
        self.rodzaj = rodzaj
        self.grubosc = grubosc

    def getoprawa(self):
        return self.rodzaj

class Book:
    o1 = Oprawa("twarda",3.2)
    op = o1.getoprawa()
    #deklaracja stanu(dane) -> konstruktor klasy
    def __init__(self,id,tytul,autor,cena=30,oprawa = op):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.oprawa = oprawa
        self.create_book()

    #definicja zachowania -> funkcje klasy -> metody
    def create_book(self):
        print("utworzono nową książkę")

    def print_book(self):
        print(f"książka {self.tytul}, autor: {self.autor}, cena: {self.cena} zł, oprawa: {self.oprawa}")

    def rabat(self,procent):
        return (1-procent/100)*self.cena

    def setcena(self,nowacena):
        self.cena = nowacena

    def gettytul(self):
        return self.tytul

b1 = Book(34,"Wiedźmin","Andrzej Sapkowski",41)
b1.print_book()
rab = float(input("podaj rabat w %: "))
print(f'rabat: {rab} % -> do zapłaty: {b1.rabat(rab):.2f} zł')
b1.setcena(45.3)
b1.print_book()
b1.oprawa = "twarda"
b1.print_book()

b2 = Book(887,"Hobbit","J.R.R. Tolkien",39)
b2.print_book()
b2.setcena(44.1)
b2.print_book()

print(f'tytuł książki: {b2.gettytul()}')
