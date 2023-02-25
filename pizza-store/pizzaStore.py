from pizza import *
class PizzaStore:
    def __init__(self) -> None:
        pass

    def orderPizza(self, typePizza):
        pizza = Pizza
        match typePizza:
            case "cheese":
                pizza = CheesePizza()
            case "greek":
                pizza = GreekPizza()
            case "pepperoni":
                pizza = PepperoniPizza() 
            case _:
                print("We do not have this pizza!!!") 
                return
        pizza.prepare()

        pizza.bake()

        pizza.cut()

        pizza.box()