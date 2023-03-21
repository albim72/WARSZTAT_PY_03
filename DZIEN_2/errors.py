try:
    print(x)
except NameError:
    print("x nie jest zdefiniowany")
    x = int(input("podaj wartość x: "))
except TypeError as d:
    print(d)
except:
    print("nieokreślony błąd")
else:
    print(f"opis x")
finally:
    y = 99
    print(y)
    print(f"twoje x wynosi {x}")


print("jestem poza instrukcją")
