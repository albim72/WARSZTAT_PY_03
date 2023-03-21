from pojazd import Pojazd

p = Pojazd()
odl = float(input("podaj odelgłość w [km]: "))
lt = float(input("podaj liczbę spalonych litrów: "))
cn = float(input("podaj cenę za 1 litr paliwa: "))
print(f"spalanie [l/100 km]: {p.spalanie(odl,lt):.2f}")
print(f"koszty przejazdu na trasie {odl} km wynoszą: {p.kosztprzejazdu(odl,lt,cn):.2f} zł")
