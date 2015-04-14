class Vehicle:
    def __init__(self):
        self.tires = 4
        
    def pop_tire(self):
        self.tires -= 1
        
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.trunk_is_open = False
    
    def toggle_trunk(self):
        self.trunk_is_open = not self.trunk_is_open

class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.bed_is_loaded = False
    
    def toggle_bed(self):
        self.bed_is_loaded = not self.bed_is_loaded
        
class Bicycle(Vehicle):
    def __init__(self):
        self.tires = 2


car = Car()
car.toggle_trunk
print(car.trunk_is_open)

truck = Truck()
truck.pop_tire()
print(truck.tires)
