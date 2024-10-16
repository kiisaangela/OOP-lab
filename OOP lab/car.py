from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, color,has_winter_tyres=False):
        super().__init__(color)
        self.has_winter_tyres = has_winter_tyres

    def toString(self):
        return super().toString() + f"\nHas winter tyres: {self.has_winter_tyres}"

