from osoba import Osoba
from sport import Sport
from klub import Klub

class Klient(Osoba,Sport,Klub):
    def __init__(self,id_klienta, imie, wiek, waga, wzrost, nr_szafki,
                 dyscyplina,lata_upr,zyciowka,nr_kb,nazwa_kb,miasto):
        Osoba.__init__(self,imie, wiek, waga, wzrost)
        Sport.__init__(self,dyscyplina,lata_upr,zyciowka)
        Klub.__init__(self,nr_kb,nazwa_kb,miasto)
        self.id_klienta = id_klienta
        self.nr_szafki = nr_szafki
        self.numerklienta()

    def numerklienta(self):
        print(f"przydzielono numer klienta: {self.id_klienta}, numer szafki: {self.nr_szafki}")
