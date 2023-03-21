def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f"element listy {lista.__name__} nr {i} -> wartość: {j}")
        
def czytaj_slownik(slownik):
    for x,y in slownik.items():
        print(f"słownik {slownik.__name__}, klucz: {x}, wartość: {y}")
