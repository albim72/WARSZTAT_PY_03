from tyrion import Tyrion

class Cersei(Tyrion):
    def walka(self):
        pass

    def negocjacja(self):
        super().negocjacja()

    def uczta(self):
        print(f"{self.tytul} jedzie na ucztę...")
