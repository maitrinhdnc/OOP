from abc import ABC
class Pizza(ABC):
    def __init__(self, name, dough=None, sauce=None, toppings=[]):
        self._name = name
        self._dough = dough
        self._sauce = sauce
        self._toppings = toppings

    def prepare(self):
        print(f"Preparing: {self._name}")
        print(f"Tossing tough...")
        print(f"Adding Sauce...")
        print("Adding Toppings: ")
        for i in self._toppings:
            print(f"{i}", end ="\n")
        print("-------------------")

    def bake(self):
        print(f"Baking {self._name} in 30 mins")

    def cut(self):
        print(f"Cutting {self._name}")

    def box(self):
        print(f"Boxing {self._name}")

class CheesePizza(Pizza):
    def __init__(self):
        self._name = "The best cheese pizza"
        self._dough = "thin dough"
        self._sauce = 'spicy'
        self._toppings = ["olives", "cheese"]

class GreekPizza(Pizza):
    def __init__(self):
        self._name = "The best greek pizza"
        self._dough = "thick dough"
        self._sauce = 'chillie'
        self._toppings = ["olives", "onions"]

class PepperoniPizza(Pizza):
    def __init__(self):
        self._name = "The best pepperoni pizza"
        self._dough = "thick dough"
        self._sauce = 'pepper'
        self._toppings = ["onions", "cheese"]