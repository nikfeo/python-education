"""
The task:
- practice creating classes from scratch and inheriting from other classes
- create a Transport class, think about attributes and methods, add them to the class
- think over and implement the class inheriting from the Transport class (at least 4),
override the methods and attributes for each class
"""


class Transport:
    """Creates base class Transport with 2 static attributes: kind and color"""

    def __init__(self, kind: str, color: str):
        self.kind = kind
        self.color = color

    def move(self, distance: int):
        """Moves vehicles a certain distance attribute"""
        return f"{self.color} {self.kind} moved {distance} km"

    @staticmethod
    def start():
        """Starts engine!"""
        return 'Engine started'

    @staticmethod
    def stop():
        """Stops engine!"""
        return 'Engine stopped'


class Car(Transport):
    """Creates class Car which inherits from class Transport"""

    def __init__(self, kind: str, color: str, number: int, fuel_type: str):
        super().__init__(kind, color)
        self.number = number
        self.fuel_type = fuel_type
        self.wheels = 4


class Bicycle(Transport):
    """Creates class Bicycle which inherits from class Transport"""

    def __init__(self, kind, color):
        super().__init__(kind, color)
        self.wheels = 2

    def start(self):
        """Starts pedaling!"""
        return f"{self.kind} has no engine. Just pedal!"

    @staticmethod
    def stop():
        """Stops pedaling!"""
        return "Do not forget to put your foot on something after stopping!"


class Plane(Transport):
    """Creates class Plane which inherits from class Transport"""

    def __init__(self, kind: str, color: str, max_height: int):
        super().__init__(kind, color)
        self.max_height = max_height
        self.wheels = 0

    def fly(self, height):
        """The plane will gain the altitude specified in the attribute"""
        return f"{self.color} {self.kind} gained altitude {height} m"

    def land(self):
        """Lands the plane"""
        return f"{self.color} {self.kind} has landed"


class Motorcycle(Bicycle, Transport):
    """Creates class Motorcycle which inherits from classes Transport and Bicycle"""

    def __init__(self, kind, color, number, fuel_type):
        Transport.__init__(self, number, fuel_type)
        super().__init__(kind, color)

    @staticmethod
    def start():
        """Starts engine!"""
        return 'Engine started'


car_green = Car("Car", "Green", 7834, "gasoline")
bicycle_grey = Bicycle("Bicycle", "Grey")
white_plain = Plane("Plane", "White", 10000)
black_moto = Motorcycle("Motorcycle", "Black", 3490, "gasoline")

print(f"\n{car_green.kind} has {car_green.wheels} wheels")
print(f"{car_green.start()}")
print(car_green.move(90))
print(f"{car_green.stop()}\n")

print(f"{bicycle_grey.kind} has {bicycle_grey.wheels} wheels")
print(bicycle_grey.start())
print(bicycle_grey.move(10))
print(f"{bicycle_grey.stop()}\n")

print(f"{white_plain.kind} has {white_plain.wheels} wheels")
print(white_plain.start())
print(f"{white_plain.fly(5000)}\n{white_plain.move(600)}")
print(white_plain.land())
print(f"{white_plain.stop()}\n")

print(f"{black_moto.kind} has {black_moto.wheels} wheels")
print(black_moto.start())
print(black_moto.move(65))
print(black_moto.stop())
