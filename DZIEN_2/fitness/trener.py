from klient import Klient

class Trener(Klient):
    def __init__(self, id_klienta, imie, wiek, waga, wzrost, nr_szafki, 
                 nr_licencji, doswiadczenie_lata, expert, dyscyplina, lata_upr, zyciowka, nr_kb, nazwa_kb,miasto):
        super().__init__(id_klienta, imie, wiek, waga, wzrost, nr_szafki, dyscyplina, lata_upr, zyciowka, nr_kb,
                         nazwa_kb, miasto)
        self.nr_licencji = nr_licencji
        self.doswiadczenie_lata = doswiadczenie_lata
        self.expert = expert
        
        
    def infotrener(self):
        return f"TRENER -> nr licencji: {self.nr_licencji}, doświadczenie w latach: {self.doswiadczenie_lata}," \
               f"czy trener jest ekspertem? -> {self.expert}"
