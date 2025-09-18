# smartphone.py

# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Inherited class (Smartphone)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # inheritance from Device
        self.__storage = storage         # encapsulated attribute
        self.__battery = battery         # encapsulated attribute

    def call(self, number):
        print(f"Calling {number} from {self.device_info()}...")

    def get_storage(self):
        return self.__storage

    def set_storage(self, new_storage):
        if new_storage > 0:
            self.__storage = new_storage

    def get_battery(self):
        return self.__battery


# Example usage
phone = Smartphone("Samsung", "Galaxy S24", 256, "85%")
print(phone.device_info())  # Output: Samsung Galaxy S24
phone.call("+254712345689")
print("Storage:", phone.get_storage(), "GB")
print("Battery:", phone.get_battery())


# polymorphism.py

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")


class Car(Vehicle):
    def move(self):
        print("Driving on the road...")


class Plane(Vehicle):
    def move(self):
        print("Flying in the sky...")


class Boat(Vehicle):
    def move(self):
        print("Sailing on the water...")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Each outputs a different action (polymorphism in action!)

