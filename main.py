# text = 'азбука'
# answer_text = ''
# answer_text_final = ''
# failed_count = 0



# while True:
#     char = input('Скажите букву: ')

#     if char in text:
#         if char in answer_text or char in answer_text_final:
#             print('Буква уже угадана')
#         else:
#             if answer_text != '':
#                 for i, a in enumerate(answer_text):
#                     if a != '*':
#                         answer_text_final += a
#                     else:
#                         char_index = text.index(char)
#                         if i == char_index:
#                             answer_text_final += text[i]
#                         else:
#                             answer_text_final += '*'
#                 print(f'Буква {char} есть в слове')
#                 print(answer_text)           
                            
                            
#             else:                
#                 for c in text:
#                     if c == char:
#                         answer_text += char
#                     else:
#                         answer_text += '*'
                        
#                 print(f'Буква {char} есть в слове')
#                 print(answer_text)





# text = 'азбука'

# text_stars = '*' * len(text)
# print(text_stars)

# while True:
# #     char = input('Скажите букву: ')
# #     if char in text:
# #         for i, c in enumerate(text):
# #             if char == c:
# #                 text_stars.replace('*', char)
# #             else:
# #                 continue
    
# #     print(text)


# class TriangleChecker:
    
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
        
        
#     def is_triangle(self):
#         if isinstance (self.__a, str) or \
#              isinstance(self.__b, str) or \
#                 isinstance(self.__b, str):
#             print('нужно вводить только числа')
#         elif self.__a < 0 or self.__b < 0 or self.__c < 0:
#             print('С отрицательными числами ничего не выйдет')
        
#         elif (self.__a + self.__b) > self.__c and \
#             (self.__a + self.__c) > self.__b and \
#             (self.__b + self.__c) > self.__a:
#                 print('Ура можно сделать треугольник')
#         else:
#             print('жаль но из этого треугольник не сделать')
            
        
#     def set_a(self, value):
#         if isinstance(value, str):
#             print('Метод принимае только числовые значкние')
#         else:
#             self.__a = value
    
#     def get_a(self):
#         return self.__a
    
    
    
#     def set_b(self, value):
#         if isinstance(value, str):
#             print('Метод принимае только числовые значкние')
#         else:
#             self.__b = value
    
#     def get_b(self):
#         return self.__b
    
    
    
#     def set_c(self, value):
#         if isinstance(value, str):
#             print('Метод принимае только числовые значкние')
#         else:
#             self.__c = value
    
#     def get_c(self):
#         return self.__c


# triangle = TriangleChecker(4,6,8)

# triangle.is_triangle()

# from math import pi

# class Shape:
#     def __init__(self, name):
#         self.name = name
        
#     def get_area(self):
#         pass
    
    
# class Triangle(Shape):
#     def __init__(self, name, height, a, b, c):
#         super().__init__(name)
#         self.__a = a
#         self.__b = b
#         self.__c = c
#         self.__height = height
        
#     def get_area(self):
#         return (1/2) * self.__a * self.__height
    
    
# class Circle(Shape):
#     def __init__(self, name, radius):
#         super().__init__(name)
#         self.__radius = radius
        
#     def get_area(self):
#         return pi * (pow(self.__radius, 2))