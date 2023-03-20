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
