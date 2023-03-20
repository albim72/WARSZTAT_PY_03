print("kolekcje języka python")
#zwykły komentarz
"""
komemntarz wieloliniowy
dokumentacyjny
"""

"""
komemntarz wieloliniowy
nie dokumentacyjny
"""
#kolekcja -> listy
imiona = ["Jan","Leon","Olga","Tytus","Roma","Edyta","Jan","Olga","Jan"]
print(imiona)
print(imiona[0])
print(imiona[:3])
print(imiona[4:])
print(imiona[-1])

w = "kalejdoskop"
print(w)
print(w[1])
print(w[2:4])
print(imiona[3][2])

imionaparzyste = imiona[1:6:2]
print(imionaparzyste)

imie = "Urszula"
odimie = imie[::-1]
print(odimie)
# imiona.sort()
# print(imiona)
print(sorted(imiona))
print(imiona)

print("________________________________________")
ip = imionaparzyste

ip_0 = list(imionaparzyste)
ip_1 = imionaparzyste[:]
print(ip)
print(imionaparzyste)
print(ip_0)
print(ip_1)

ip[:] = [5,88,9,77]
print("________________________________________")
print(ip)
print(imionaparzyste)

print(ip==imionaparzyste)

print(ip_0)
print(ip_1)

print(ip==ip_1)
