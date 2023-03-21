def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f"element listy nr {i} -> wartość: {j}")

def czytaj_slownik(slownik):
    for x,y in slownik.items():
        print(f"słownik, klucz: {x}, wartość: {y}")
