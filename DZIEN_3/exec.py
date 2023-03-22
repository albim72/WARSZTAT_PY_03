import os

mojkod = '''
a=5
b=4
print(f"wynik działania a*b+2: {a*b+2}")
'''
exec(mojkod)

code = input("Co chcesz dzisiaj zrobić?")
exec(code)

print("_____________________________________")

def calc_perimeter(l):
    return 4*l

def calc_area(l):
    return l**2

expr = input("podaj funkcję: ")
for l in range(1,5):
    if(expr == 'calc_perimeter(l)'):
        print(f"Jeśli długość boku działki wynosi {l} to jej obwód = {eval(expr)}")
    elif (expr == 'calc_area(l)'):
        print(f"Jeśli długość boku działki wynosi {l} to jej pole powierzchni = {eval(expr)}")
    else:
        print('takie działanie nie istnieje!')
        break
