import json

jsonbook = '{"tytuł":"Hobbit","autor":"J.R.R. Tolkien","oprawa":"twarda","lstron":288,"cena":37.88,"filie":[5,7,8,11,23,45]}'
print(jsonbook)
print(type(jsonbook))

book = json.loads(jsonbook)
print(type(book))
print(book["autor"])
print(book["filie"][2])

def parser(opis,source,key,index=None):
    print(opis,end="")
    if index == None:
        print(source[key])
    else:
        print(source[key][index])

parser("filia księgarni pozycja -> 3: ",book,"filie",3)
parser("Tytuł książki: ",book,"tytuł")
