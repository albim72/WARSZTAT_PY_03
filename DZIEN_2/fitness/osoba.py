class Osoba:
    def __init__(self,imie,wiek,waga,wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.kolor_oczu = "brązowe"
        
    def print_osoba(self):
        print(f"osoba -> {self.imie}, wiek: {self.wiek}, waga: {self.waga} kg, "
              f"wzrost: {self.wzrost} cm, kolor oczu: {self.kolor_oczu}")
        
    def setkolor(self,nkolor):
        self.kolor_oczu = nkolor
        
    def wiek_za_n_lat(self,n):
        return f"wiek za {n} lat: {self.wiek+n}"
