#Automóvil

class Car:
    def __init__(self):
        self.model = ""
        self.color = ""
        self.features = []

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Features: {', '.join(self.features)}")

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_model(self, model):
        self.car.model = model

    def set_color(self, color):
        self.car.color = color

    def add_feature(self, feature):
        self.car.features.append(feature)

    def get_car(self):
        return self.car

# Uso del Builder
car_builder = CarBuilder()
car_builder.set_model("Sedan")
car_builder.set_color("Blue")
car_builder.add_feature("Leather Seats")
car_builder.add_feature("Sunroof")

car = car_builder.get_car()
car.display_info()
