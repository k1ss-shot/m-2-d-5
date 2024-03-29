# '''Задача 1: Инкапсуляция - Класс Счет

# Создайте класс Account с приватным атрибутом balance (баланс)
# и методами для депозита и снятия средств, а также для получения текущего баланса.'''



# class Account:
    
#     def __init__(self, balance):
#         self.__balance = balance
        
    
#     def deposite (self):
        
#         try:
#             deposite = float(input('Внесите сумму для депозита: '))
            
#         except ValueError:
#             print('Пожалуйста используйте только цифры')
        
#         else:
#             self.__balance += deposite
#             print('Ваш депозит прошел успешно')
            
            
#     def withdraw_fund(self): #с английского пероводиться как "снять стредство"
        
#         try:
#             print('Укажите сумму которую хотите снять: ')
#             sredstva = float(input())
        
#         except ValueError:
#             print('Пожалуйста используйте только цифры')
            
#         else:
#             self.__balance -= sredstva
#             print('Вы успено провели операцию')

#     def print_balance(self):
     
#         print(f'ваш баланс {self.__balance}')
        


# my_balance = Account(balance=10000)

# my_balance.deposite()
# my_balance.withdraw_fund()
# my_balance.print_balance()


'''Задача 2: Полиморфизм - Классы Животных

Создайте классы Dog и Cat, оба наследуют от класса Animal. 
Каждый из классов должен иметь метод speak, который возвращает разные звуки для собаки и кошки.'''


# class Animal:
    
#     def __init__(self, animal):
#         self.__animal = animal
        
#     def speak():
#         pass
    
# class Dog(Animal):
    
#     def __init__(self):
        # super().__init__(animal)
        
#     def speak(self):
#         print('Гав-гав')
        
# class Cat(Animal):
    
#     def __init__(self):
        # super().__init__(animal)
        
#     def speak(self):
#         print('Мяу-мяу')
        
        
# dog = Dog()
# dog.speak()
# cat = Cat()
# cat.speak()


'''Задача 3: Класс Фигура

Создайте класс Shape с методом area, который возвращает площадь.#
Создайте производные классы, такие как Rectangle и Circle, переопределяющие метод area.'''

# from math import pi

# class Shape:
#     def __init__(self):
#         pass
        
#     def get_area(self):
#         pass
    
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.__radius = radius
        
#     def get_area(self):
#         return print(pi * (pow(self.__radius, 2)))
    
    
# class Rectangle(Shape):
#     def __init__(self, lenght, widht):
#         self.__lenght = lenght
#         self.__widht = widht
        
#     def get_area(self):
#         return print(self.__lenght * self.__widht)
    
    
# rectangle = Rectangle(lenght=20, widht=10)
# rectangle.get_area()
# circle = Circle(radius=10)
# circle.get_area()



'''Задача 4: Композиция - Класс Комната

Создайте класс Room с атрибутами, представляющими список мебели. Используйте композицию,
создав отдельные классы для разных типов мебели, и добавьте их в класс Room.'''


# class Room:
#     def __init__(self):
#         self.furniture = []  

#     def add_furniture(self, furniture):
#         self.furniture.append(furniture)

#     def describe_furniture(self):
#         print("Мебель в комнате:")
#         for item in self.furniture:
#             print("-", item)

# class Furniture:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

# class Chair(Furniture):
#     def __init__(self, name):
#         super().__init__(name)

# class Table(Furniture):
#     def __init__(self, name):
#         super().__init__(name)

# class Lamp(Furniture):
#     def __init__(self, name):
#         super().__init__(name)

# class Sofa(Furniture):
#     def __init__(self, name):
#         super().__init__(name)


# room = Room()


# chair1 = Chair('кресло')
# table1 = Table('стол')
# lamp1 = Lamp('лампа')
# sofa1 = Sofa('диван')


# room.add_furniture(chair1)
# room.add_furniture(table1)
# room.add_furniture(lamp1)
# room.add_furniture(sofa1)


# room.describe_furniture()




'''Задача 5: Абстрактный Класс - Устройство

Создайте абстрактный класс Device с абстрактным методом turn_on. 
Создайте производные классы, такие как Laptop и Smartphone, реализующие метод turn_on.'''



class Device:
        
    def turn_on(self):
        pass
    
class Laptop(Device):
    
    def turn_on(self):
        print('Включение ноутбука')

class Smartphone(Device):
    
    def turn_on(self):
        print('Включение смартфона')
        

laptop1 = Laptop()
laptop1.turn_on()
smartphone1 = Smartphone()
smartphone1.turn_on()
