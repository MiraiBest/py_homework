# Реализуйте алгоритм перемешивания списка.
import random
from random import randint


def _list(n):
    _list = []
    for i in range(n):
        _list.append(randint(-n, n + 1))
    return _list


n = int(input('Введите число: '))
new_list = _list(n)
print(new_list)
random.shuffle(new_list)
print('->', new_list)
