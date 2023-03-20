#przyklad 1
import random


def user(nazwa):
    return f"nazwa użytkownika: {nazwa}"

def przelew(nazwa,kwota,data):
    return f"Dane przelewu -> użytkownik: {nazwa}, data wykonania przelewu: {data}, kwota: {kwota} zł."

def konto(funkcja,*args):
    return funkcja(*args)

print(konto(user,"Marta"))
print(konto(przelew,"Leon",13200,"2023-03-10"))

#przykład 2
def przejazd(oplata):
    def _bilet():
        return "kontrola biletów: OK"

    def _brak():
        return "kontrola biletów: kara finansowa"

    def _error():
        return "błąd odczytu kodu biletu. Spróbuj ponownie (1-opłacony, 0-brak)"

    if oplata == 1:
        return _bilet
    elif oplata == 0:
        return _brak
    else:
        return _error

print(przejazd(1)())
print(przejazd(0)())
print(przejazd(-3)())

#przykład 3

def opakowanie(funkcja):
    def wrapper(*args):
        print("opakowanie funkcji wywoływanej przez funkcję opakowanie...")
        funkcja(*args)
        n = random.random()*100
        print(f"po wykonaniu funkcji {funkcja.__name__} losujemy wartość n -> {round(n)}")
    return wrapper

def jazda(pojazd):
    print(f"jazda z użyciem pojazdu: {pojazd}")
print("_______________________________________________")
p = opakowanie(jazda)
p("rower")

@opakowanie
def obliczenie(a,b,c):
    wynik = a+b**c
    print(f'wynik działania: {wynik}')

print("_______________________________________________")
obliczenie(5,8,3)




