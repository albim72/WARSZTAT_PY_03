marka = "Jeep"
model = "Cherokee"
rocznik = 2020
sam = "samochód -> marka: {}, model: {}, rocznik: {}."
print(sam.format(marka,model,rocznik))

sam1 = "samochód -> rocznik: {2}, marka: {0}, model: {1}."
print(sam1.format(marka,model,rocznik))

#f-string

print(f"autkomis -> samochód {marka} z rocznika {rocznik}, model: {model}")

konkurs = [
    ("Jan",53),
    ("Anna",45),
    ("Leon",33),
    ("Olga",50),
    ("Janina",60),
    ("Kuneggunda",56)
]

print("____________________________________")
print(list(enumerate(konkurs)))

print("_______ zestawienie wyników konkursowych _________")
for i,(imie,punkty) in enumerate(konkurs):
    print('nr %d: %-11s : %.1f punktów' %(i+1,imie,punkty))
