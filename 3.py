# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

my_list = []
for i in range(random.randint(3, 10)):
    index = (random.randint(0, 3))
    my_list.append(round(random.uniform(1, 10), index))
print(my_list)
my_min = 1
my_max = round(my_list[0] % 1, 3)
result = 0
for i in range(1, len(my_list)):
    if 0 < my_list[i] % 1 < my_min:
        my_min = round(my_list[i] % 1, 3)
    elif 0 < my_list[i] % 1 > my_max:
        my_max = round(my_list[i] % 1, 3)
result = round(my_max - my_min, 3)
print(f'{my_max} - {my_min} = {result}')
