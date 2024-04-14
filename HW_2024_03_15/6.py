# Написать программу, которая определяет представляет ли строка двоичное число.

# Программа получает из stdin строку, содержащую один из нескольких возможных форматов строкового представления двоичного числа: без префикса, префикс 'b', префикс '0b'. 
# Например:
#     0101
#     b11
#     0b11001

# Программа выводит в stdout текстовый ответ.

# В этой задаче необходимо использовать множества.

# Пример ввода:
#     1b0101

# Пример вывода:
#     нет
binary = {"0", "1"}

string = input()

if string.startswith('0b'):
    string = string[2:]

if string.startswith('b'):
    string = string[1:]

if set(string) <= binary:
    print("да")
else:
    print("нет")