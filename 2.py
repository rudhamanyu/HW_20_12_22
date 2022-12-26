# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
import math
import random

my_list = []
result_list = []
for i in range(random.randint(3, 10)):
    my_list.append(random.randint(1, 10))

for i in range(math.ceil(len(my_list) / 2)):
    result_list.append(my_list[i] * my_list[-1 - i])
print(f'{my_list} => {result_list}')
