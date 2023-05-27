# Задание 1
# Создайте реализацию паттерна Builder. Протестируйте
# работу созданного класса.

# class Coffee:
#     def __init__(self):
#         self.hot_water = False
#         self.cold_water = False
#         self.coffee = False
#         self.milk = False
#         self.icecream = False
#         self.espresso = []
#         self.latte = []
#         self.cappuccino = []
#         self.glace = []
#
#     def __str__(self):
#         string = ""
#         if self.hot_water:
#             string += "HOT "
#         if self.cold_water:
#             string += "ICE "
#         if self.coffee:
#             string += "COFFEE "
#         if self.milk:
#             string += "WITH MILK\n"
#         if self.icecream:
#             string += "WITH ICECREAM\n"
#         else:
#             string += "COFFEE\n"
#
#         if self.espresso:
#             string += "Espresso is preparing!..\n"
#         for module in self.espresso:
#             string += "- " + str(module) + "\n"
#         if self.latte:
#             string += "Latte is preparing!..\n"
#         for module in self.latte:
#             string += "- " + str(module) + "\n"
#         if self.cappuccino:
#             string += "Cappuccino is preparing!..\n"
#         for module in self.cappuccino:
#             string += "- " + str(module) + "\n"
#         if self.glace:
#             string += "Glace is preparing!..\n"
#         for module in self.glace:
#             string += "- " + str(module) + "\n"
#         return string
#
#
# class HotCoffee:
#     def __str__(self):
#         return 'hot'
#
#
# class IceCoffee:
#     def __str__(self):
#         return 'ice'
#
#
# class BlackCoffee:
#     def __str__(self):
#         return "coffee"
#
#
# class WithMilk:
#     def __str__(self):
#         return "milk"
#
#
# class Sweet:
#     def __str__(self):
#         return "sugar"
#
#
# class Icecream:
#     def __str__(self):
#         return "icecream"
#
#
# from abc import ABC, abstractmethod
#
#
# class CoffeeMachine(ABC):
#     @abstractmethod
#     def reset(self):
#         pass
#
#     @abstractmethod
#     def make_coffee(self):
#         pass
#
#     @abstractmethod
#     def add_sugar(self):
#         pass
#
#
# class Espresso(CoffeeMachine):
#     def __init__(self):
#         self.product = Coffee()
#
#     def reset(self):
#         self.product = Coffee()
#
#     def get_product(self):
#         return self.product
#
#     def make_coffee(self):
#         self.product.hot_water = True
#         self.product.coffee = True
#         self.product.espresso = True
#
#     def add_sugar(self):
#         self.product.espresso.append(Sweet)
#
#
# class Glace(CoffeeMachine):
#     def __init__(self):
#         self.product = Coffee()
#
#     def reset(self):
#         self.product = Coffee()
#
#     def get_product(self):
#         return self.product
#
#     def make_coffee(self):
#         self.product.cold_water = True
#         self.product.coffee = True
#         self.product.icecream = True
#         self.product.glace.append(IceCoffee)
#         self.product.glace.append(BlackCoffee)
#         self.product.glace.append(Icecream)
#
#     def add_sugar(self):
#         self.product.glace.append(Sweet)
#
#
# coffee = Glace()
# coffee.make_coffee()
# coffee.add_sugar()
# print(coffee.get_product())


# coffee = Espresso()
# coffee.make_coffee()
# coffee.add_sugar()
# print(coffee.get_product())


# Задание 2. Интересная задача, но я так долго с ней возилась.. Почти неделю! Пока не прочувствовала каждое слово кода))
# Создайте приложение для приготовления пасты. Приложение должно уметь создавать минимум три вида пасты.
# Классы различной пасты должны иметь следующие
# методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.

# from abc import ABC, abstractmethod
#
#
# class Spaghetti(ABC):
#
#     @abstractmethod
#     def cook_pasta(self):
#         pass
#
#     @abstractmethod
#     def cook_sauce(self):
#         pass
#
#     @abstractmethod
#     def supplement(self):
#         pass
#
#
# class Ravioli(ABC):
#
#     @abstractmethod
#     def make_pasta(self):
#         pass
#
#     @abstractmethod
#     def filling(self):
#         pass
#
#     @abstractmethod
#     def cook_pasta(self):
#         pass
#
#     @abstractmethod
#     def cook_sauce(self):
#         pass
#
#     @abstractmethod
#     def supplement(self):
#         pass
#
#
# class Penne(ABC):
#
#     @abstractmethod
#     def cook_pasta(self):
#         pass
#
#     @abstractmethod
#     def cook_sauce(self):
#         pass
#
#     @abstractmethod
#     def supplement(self):
#         pass
#
#
# class Cappellacci(ABC):
#
#     @abstractmethod
#     def make_pasta(self):
#         pass
#
#     @abstractmethod
#     def filling(self):
#         pass
#
#     @abstractmethod
#     def cook_pasta(self):
#         pass
#
#     @abstractmethod
#     def cook_sauce(self):
#         pass
#
#     @abstractmethod
#     def supplement(self):
#         pass
#
#
# class BologneseSpaghetti(Spaghetti):
#     def make_pasta(self):
#         pass
#
#     def filling(self):
#         pass
#
#     def cook_pasta(self):
#         print('Сварить спагетти')
#
#     def cook_sauce(self):
#         print('Добавить соус болоньезе')
#
#     def supplement(self):
#         print('Посыпать сыром и измельчённым базиликом')
#
#
# class BolognesePenne(Penne):
#
#     def make_pasta(self):
#         pass
#
#     def filling(self):
#         pass
#
#     def cook_pasta(self):
#         print('Сварить пенне')
#
#     def cook_sauce(self):
#         print('Добавить соус болоньезе')
#
#     def supplement(self):
#         print('Посыпать сыром и измельчённым базиликом')
#
#
# class CarbonaraSpaghetti(Spaghetti):
#
#     def make_pasta(self):
#         pass
#
#     def filling(self):
#         pass
#
#     def cook_pasta(self):
#         print('Сварить спагетти')
#
#     def cook_sauce(self):
#         print('Добавить соус карбонара')
#
#     def supplement(self):
#         print('Посыпать сыром и измельчённым орегано')
#
#
# class CarbonaraPenne(Penne):
#
#     def make_pasta(self):
#         pass
#
#     def filling(self):
#         pass
#
#     def cook_pasta(self):
#         print('Сварить пенне')
#
#     def cook_sauce(self):
#         print('Добавить соус карбонара')
#
#     def supplement(self):
#         print('Посыпать сыром и измельчённым орегано')
#
#
# class RavioliShrimp(Ravioli):
#
#     def make_pasta(self):
#         print('Лепим равиоли')
#
#     def filling(self):
#         print('Начинка - креветки')
#
#     def cook_pasta(self):
#         print('Сварить равиоли')
#
#     def cook_sauce(self):
#         print('Добавить соус бешамель')
#
#     def supplement(self):
#         print('Посыпать сыром и измельчённым орегано')
#
#
# class RavioliMeat(Ravioli):
#
#     def make_pasta(self):
#         print('Лепим равиоли')
#
#     def filling(self):
#         print('Начинка - мясной фарш')
#
#     def cook_pasta(self):
#         print('Сварить равиоли')
#
#     def cook_sauce(self):
#         print('Добавить соус томатный')
#
#     def supplement(self):
#         print('Посыпать сыром и измельчённой петрушкой')
#
#
# class CappellacciPumpkin(Cappellacci):      # у этой пасты начинка бывает только из тыквы
#
#     def make_pasta(self):
#         print('Лепим каппеллаччи')
#
#     def filling(self):
#         print('Начинка - тыква')
#
#     def cook_pasta(self):
#         print('Сварить каппеллаччи')
#
#     def cook_sauce(self):
#         print('Добавить бульон')
#
#     def supplement(self):
#         print('Посыпать сыром и измельчённой петрушкой')
#
# class AbstractFactory(ABC):
#
#     @abstractmethod
#     def create_pasta(self):
#         pass
#
#
# class PastaBologneseSpaghetti(AbstractFactory):
#
#     def create_pasta(self):
#         return BologneseSpaghetti()
#
#
# class PastaBolognesePenne(AbstractFactory):
#
#     def create_pasta(self):
#         return BolognesePenne()
#
#
# class PastaCarbonaraSpaghetti(AbstractFactory):
#
#     def create_pasta(self):
#         return CarbonaraSpaghetti()
#
#
# class PastaCarbonaraPenne(AbstractFactory):
#
#     def create_pasta(self):
#         return CarbonaraPenne()
#
#
# class PastaRavioliShrimp(AbstractFactory):
#     def create_pasta(self):
#         return RavioliShrimp()
#
#
# class PastaRavioliMeat(AbstractFactory):
#     def create_pasta(self):
#         return RavioliMeat()
#
#
# class PastaCappellacci(AbstractFactory):
#
#     def create_pasta(self):
#         return CappellacciPumpkin()
#
#
# def main():
#     for factory in (PastaBologneseSpaghetti(), PastaBolognesePenne(), PastaCarbonaraSpaghetti(), PastaCarbonaraPenne(),
#                     PastaRavioliShrimp(), PastaRavioliMeat(), PastaCappellacci()):
#         product_a = factory.create_pasta()
#         print(product_a)
#         product_a.make_pasta()
#         product_a.filling()
#         product_a.cook_pasta()
#         product_a.cook_sauce()
#         product_a.supplement()
#         print("*" * 20)
#
#
# if __name__ == "__main__":
#     main()


# Задание 3
# Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса.

# from abc import ABC, abstractmethod
#
#
# class Prototype(ABC):
#
#     @abstractmethod
#     def clone(self):
#         pass
#
#
# class Stencil(Prototype):
#     def __init__(self, length, width, color):
#         self.field1 = length
#         self.field2 = width
#         self.field3 = color
#         self.performed_operation = False
#
#     def __operation__(self):
#         self.performed_operation = True
#
#     def clone(self):
#         obj = Stencil(self.field1, self.field2, self.field3)
#         obj.performed_operation = self.performed_operation
#         return obj
#
#     def __str__(self):
#         return f'Длина {self.field1}, ширина {self.field2}, цвет {self.field3}'
#
#
# stencil_a = Stencil(10, 15, 'green')
# stencil_b = Stencil(20, 20, 'black')
#
# a = stencil_a.clone()
# b = stencil_b.clone()
# c = stencil_b.clone()
# print(a)
# print(b)
# print(c)
