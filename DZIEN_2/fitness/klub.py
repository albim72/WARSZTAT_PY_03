class Klub:
    
    def __init__(self,nr_kb,nazwa_kb,miasto):
        self.nr_kb = nr_kb
        self.nazwa_kb = nazwa_kb
        self.miasto = miasto
        self.przypisanie_kb()
        
        
    def przypisanie_kb(self):
        print(f"przypisano do klubu nr {self.nr_kb}")
        
    def infoklub(self):
        return f"klub {self.nazwa_kb}, nr {self.nr_kb}, miasto: {self.miasto}."
