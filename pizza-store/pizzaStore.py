from pizza import *
import asyncio
class PizzaStore:
    def __init__(self) -> None:
        pass

    async def orderPizza(self, typePizza):
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
        await asyncio.sleep(1)
        pizza.prepare()

        await asyncio.sleep(1)
        pizza.bake()
       
        await asyncio.sleep(1)
        pizza.cut()
        
        await asyncio.sleep(1)
        pizza.box()