#import dane
#import dane as dn
from dane import nr_filii as filia
from dane import book as ks
from funkcje.bfunkcje import czytaj_liste, czytaj_slownik

print("________ wyświetlanie bezpośrednie ____________")
print(filia)
print(ks)

print("________ wyświetlanie za pomocą funkcji ____________")
czytaj_liste(filia)
czytaj_slownik(ks)
