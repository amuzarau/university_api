1 + 1

import os

os.getcwd()

4 * 6
22 / 7

a = 5
print(a)

3 == 3

x = [1, 2, 3]
len(x)

a = {"a": 1, "b": 2, "c": 3}
a.keys()
a.values()
a["a"]


def fun():
    print("Welcome to university!")


fun()


class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self.year = year

    def get_make(self):
        return self._make

    def set_model(self, model):
        self._model = model

    def get_model(self):
        return self._model


my_car = Car("Toyota", "Corolla", 2020)
print(my_car.get_make())
my_car.set_model("Camry")
print(my_car.get_model())
print(my_car.year)
