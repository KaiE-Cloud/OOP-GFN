class Hund:
    __art = "Canis"   # Klassenattribut (alle Hunde teilen es)

    def __init__(self, name):
        self.name = name   # Instanzattribut (jede Instanz hat eigenen Wert)


Hund_1 = Hund("Bello")
Hund_2 = Hund("Luna")

print(Hund_1._Hund__art + Hund_1.name)
print(Hund_2._Hund__art + Hund_2.name)