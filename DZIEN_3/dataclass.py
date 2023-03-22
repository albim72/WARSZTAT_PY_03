from dataclasses import dataclass

class Signal:
    def __init__(self,s,delta):
        self.s=s
        self.delta=delta

sgo = Signal(2,0.004)
print(sgo.delta)

@dataclass
class Wartosc:
    x:int
    y:int
    sigma:float

wa = Wartosc(5,7,9.3)
print(wa.y)


class Wartzw:
    x:int
    y:int
    sigma:float

wz = Wartzw()


@dataclass
class Opis:
    nazwa:str
    liczba:int
    rabat:float
    dodatki:str

    def __init__(self,nazwa,liczba):
        self.nazwa = nazwa
        self.liczba = liczba
        self.rabat = 0.1
        self.dodatki = "mocowanie"


op = Opis("kaloryfer",4)
print(op.nazwa,op.dodatki)
