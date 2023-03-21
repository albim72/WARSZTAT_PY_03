#konstruktor __missing__

class MyDict(dict):
    def __missing__(self, key):
        return "taki klucz nie istnieje"

osoby = {'Olek':45,'Olga':55,'Leon':52}
print(osoby['Olga'])
# print(osoby['Roman'])

md = MyDict(osoby)
print(md['Olga'])
print(md['Roman'])

class Funkcyjna:
    def __init__(self):
        print("Instancja została utworzona")

    def __call__(self, info):
        print(f"Instancja wołana przez __call__ zwraca komunikat: {info}")
        


ng = Funkcyjna()
ng("niewykle waża wiadmość")
