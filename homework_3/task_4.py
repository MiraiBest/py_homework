# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input('Введите число: '))

nbin = ''

while n > 0:
    nbin = str(n % 2) + nbin
    n = n // 2

print(nbin)
