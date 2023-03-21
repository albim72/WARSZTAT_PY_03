from abc import ABC,abstractmethod

class Prototyp(ABC):
    def __init__(self,x):
        self.x=x

    def msg(self):
        print("metoda nieabstrakcyjna klasy abstrakcyjnej")

    @abstractmethod
    def policz(self):
        pass

    @abstractmethod
    def policz_x(self):
        return 5*self.x


class Regular(Prototyp):

    def __init__(self, x,y):
        super().__init__(x)
        self.y=y

    def policz(self):
        return 1001

    def policz_x(self):
        return super().policz_x()+3*(self.y/(22+self.x))


r = Regular(3,8)
print(r.policz())
print(r.policz_x())
