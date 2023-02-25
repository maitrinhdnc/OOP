from pizzaStore import PizzaStore
import asyncio

# async def main():
#     pizzaStore = PizzaStore()
#     task1 = asyncio.create_task(pizzaStore.orderPizza("cheese"))
#     task2 = asyncio.create_task(pizzaStore.orderPizza("greek"))
#     await task1
#     await task2

if __name__ == '__main__':

    # asyncio.run(main())

    pizzaStore = PizzaStore()
    pizzaStore.orderPizza("cheese")
    pizzaStore.orderPizza("greek")