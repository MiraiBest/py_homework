# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Добавьте возможность использования скобок, меняющих приоритет операций.

print('Введите арифметическое выражение: ')
str = input()
print(f'Результат: {eval(str)}')
