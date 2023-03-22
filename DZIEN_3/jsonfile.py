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

kolor = {
    "id":985473453,
    "nazwa koloru":"żółty ciemny",
    "paleta":"UKL56453",
    "liczba odcieni":12
}

jsoncolor = json.dumps(kolor,indent=4)
print(jsoncolor)

with open("kolor.json","w",encoding="utf-8") as f:
    f.write(jsoncolor)

with open("kolor.json","r",encoding="utf-8") as f:
    kolor_dict = json.load(f)

print(kolor_dict)
print(type(kolor_dict))

print("____________________________________________")

instytut = '{"organizacja":"BIOTECH SA","miasto":"Krosno","kraj":"Polska"}'
projekt = {"id_proj":565565,"zakres":"algorytmy AI",
           "tytuł":"Nowe algorytmy używane w zakresie analizy związków chemicznych","miejsce":"Krosno Lab"}

inst = json.loads(instytut)
print(type(inst))

inst.update(projekt)
print(inst)

inst_json = json.dumps(inst, indent=4)
with open("badanie.json","w",encoding="utf-8") as f:
    f.write(inst_json)
