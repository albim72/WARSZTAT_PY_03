class Kwadrat:
    def __init__(self,bok):
        self.bok = bok

    def policzpole(self):
        return self.bok ** 2

class Prostokat:
    def __new__(cls, szer:float, wys:float):
        if szer==wys:
            return Kwadrat(bok=szer)
        return object.__new__(Prostokat)

    def __init__(self,szer:float, wys:float):
        self.szer = szer
        self.wys = wys

    def policzpole(self):
        return self.szer*self.wys

r1 = Prostokat(7.8,6)
r2 = Prostokat(5.5,5.5)

print(type(r1))
print(type(r2))

print(f'pole figury {r1.__class__.__name__} wynosi: {r1.policzpole():.2f}')
print(f'pole figury {r2.__class__.__name__} wynosi: {r2.policzpole():.2f}')

        
