from dataclasses import dataclass

class Test:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __repr__(self):
        return f'dane: a={self.a}, b= {self.b}'

t = Test(4,5)
print(t)

@dataclass
class Pojazd:
    rodzaj:str
    liczba_kol:int
    felga:float
    naped:str

@dataclass(init=False)
class Terenowy(Pojazd):
    model:str
    poj:float
    cena:float
    marka: str

    def __init__(self,model,marka="Jeep"):
        self.model = model
        self.marka = marka
        self.naped = "silnik spalinowy"
        self.poj = 4.4
        self.felga = 19
        self.cena = 234000
        self.rodzaj = "samochód"
        self.liczba_kol = 4

    def __str__(self):
        return f"całkiem ciekawy model samochodu terenowego"

    def __repr__(self):
        return f"{self.marka} {self.model}, pojemność: {self.poj}, cena: {self.cena} zł"

    def info(self):
        print(f"{self.marka} {self.model}, rozmiar felgi: {self.felga} cali")

tr = Terenowy("Cherokee")
print(tr)
tr.info()
