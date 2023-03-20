#przyklad 1
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



