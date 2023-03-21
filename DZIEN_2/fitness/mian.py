from osoba import Osoba

print("______ osoba 1 __________")
os1 = Osoba("Jan",34,88,175)
os1.print_osoba()
print(os1.wiek_za_n_lat(6))

print("______ osoba 2 __________")
os2 = Osoba("Anna",53,61,170)
os2.setkolor("niebieskie")
os2.print_osoba()
print(os2.wiek_za_n_lat(8))

print("______ osoba 3 __________")
os3 = Osoba("Leon",88,90,178)
os3.setkolor("zielone")
os3.print_osoba()
print(os3.wiek_za_n_lat(2))
