import sys


sys.set_int_max_str_digits(0x1000000)
sys.setrecursionlimit(0x1000000)
def silnia(n):
    if n<0:
        raise ValueError("silnia nie jest zdefiniowana dla liczb ujemnych!")
    wynik=1
    for i in range(1,n+1):
        wynik *= i
    return wynik

def silnia_rek(n):
    if n < 0:
        raise ValueError("silnia nie jest zdefiniowana dla liczb ujemnych!")
    if n==0:
        return 1
    else:
        return n*silnia_rek(n-1)

try:
    n = int(input("podaj wartość argumentu n funkcji silnia: "))
    print(f"silnia z wartości {n} wynosi: {silnia(n)}")
    print(f"silnia rekurencyjna z wartości {n} wynosi: {silnia_rek(n)}")
except ValueError as v:
    print(v)
