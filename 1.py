# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

my_list = []
result_sum = 0
for i in range(10):
    my_list.append(random.randint(0, 10))
    if i % 2:
        result_sum += my_list[i]
print(my_list)
print(result_sum)