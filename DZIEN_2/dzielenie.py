def dziel(x,y):
    try:
        wynik=x/y
    except ZeroDivisionError:
        print("Uwaga! dzielenie przez 0")
    except NameError:
        print("zmienne niezdefiniowane")
    except TypeError as tp:
        print(tp)
    except Exception as ex:
        print(ex)
        print(type(ex))
    else:
        print(f'wynik = {wynik}')
    finally:
        print("policzmy coś jeszcze")

try:
    dziel(9,8)
    dziel(9,0)
    dziel(0,8)
    dziel(0,0)
    dziel(5.777,0.000000000002)
    dziel(7,False)
    dziel(7,"abc")
    dziel(777)
except TypeError:
    print("zbyt mała liczba argumentów..../muszą być dwa: x,y/")
