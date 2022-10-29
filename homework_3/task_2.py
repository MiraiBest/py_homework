# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
from random import randint

num = int(input('Введите размер списка: '))
list = []
list2 = []

for i in range(num):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list) / 2 < num:
        num -= 1
        a = list[i] * list[num]
        list2.append(a)
        i += 1

print(list)
print(list2)
