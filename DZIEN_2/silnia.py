import sys


sys.set_int_max_str_digits(0x1000000)
def silnia(n):
    if n<0:
        raise ValueError("silnia nie jest zdefiniowana dla liczb ujemnych!")
    wynik=1
    for i in range(1,n+1):
        wynik *= i
    return wynik

try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    print(f"silnia z wartości {n} wynosi: {silnia(n)}")
except ValueError as v:
    print(v)
