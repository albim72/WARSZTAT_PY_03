class Sport:
    def __init__(self,dyscyplina,lata_upr,zyciowka):
        self.dyscyplina = dyscyplina
        self.lata_upr = lata_upr
        self.zyciowka = zyciowka
        self.dyscyplina_przypisanie()
        
    def dyscyplina_przypisanie(self):
        print(f"przypisano do dyscypliny: {self.dyscyplina}")
        
    def infosport(self):
        return f"{self.dyscyplina}, czas uprawiania: {self.lata_upr} lat, życiówka: {self.zyciowka}."
