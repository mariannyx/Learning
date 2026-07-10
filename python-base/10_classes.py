print("\n===== 1. Classes =====\n")


# We use classes to define a new type
class Car:
    # Constructor is used to create an obj
    def __init__(self, name, speed=100):
        self.name = name
        self.speed = speed

    # self is a reference to the current obj
    def present(self):
        print(f"\nName: {self.name} \nSpeed: {self.speed}")


# Object is an unique instance of a class
bmw = Car("BMW")
print(f"Name: {bmw.name}")

# it also have attributes that we can set anywhere
bmw.speed = 140
print(f"Speed: {bmw.speed}")

porsche = Car("Porsche", 240)
porsche.present()


print("\n===== 2. Inheritance =====\n")


# Principle called DRY - don't repeat yourself
# Inherit all the methods defined in the parent class
class Bus(Car):
    # Means and does nothing
    # pass

    # Specific constructor for the parent class
    def __init__(self, name, speed=80, passengers=50):
        super().__init__(name, speed)
        self.passengers = passengers

    def present(self):
        super().present()
        print(f"Passengers: {self.passengers}")


# Keyword argument
bus = Bus("Marshutka", passengers=55)
bus.present()
