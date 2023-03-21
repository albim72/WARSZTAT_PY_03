from tywin import Tywin
from tyrion import Tyrion
from cersei import Cersei


tyw = Tywin("Lannister","Lord","m",8,7,9)
tyr = Tyrion("Lannister","Lord","m",7,9,10)
cer = Cersei("Lannister","Królowa","k",2,10,10)

print(f"____ {tyw.tytul} {tyw.__class__.__name__} _______")
tyw.walka()
tyw.negocjacja()

print(f"____ {tyr.tytul} {tyr.__class__.__name__} _______")
tyr.walka()
tyr.negocjacja()
tyr.uczta()

print(f"____ {cer.tytul} {cer.__class__.__name__} _______")
cer.negocjacja()
cer.uczta()
