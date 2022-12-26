# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

n = int(input('Введите число: '))
my_str = ''
result = ''
while n >= 1:
    my_str += str(int(n % 2))
    n /= 2
for i in range(len(my_str)):
    result += my_str[-1 - i]
print(result)