
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

a =int(input('Введите координату X первого числа '))
b =int(input('Введите координату Y первого числа '))
c =int(input('Введите координату X второго числа '))
d =int(input('Введите координату Y второго числа '))

print(round((((a-c)**2 + (b-d)**2)**0.5)*100)/100)