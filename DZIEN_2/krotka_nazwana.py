from collections import namedtuple

Student = namedtuple('Student',['imie','nazwisko','wiek','kierunek','nralb'])

s = Student('Paweł','Kot',23,'informatyka',456)
print(f"nr albumu studenta: {s[4]}")
print(f"student {s.imie} {s.nazwisko}")
print(f"wiek studenta: {getattr(s,'wiek')}")

li = ['Olga','Nowak',21,'socjologia',988]
ns1 = Student._make(li)
print(ns1)

dc= {'imie':'Konrad','nazwisko':'Kloc','wiek':22,'kierunek':'lekarski','nralb':4356}
ns2 =  Student(**dc)
print(ns2)

sd = s._asdict()
print(sd)
