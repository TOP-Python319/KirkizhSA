# Написать программу, которая подсчитывает сумму введённых положительных чисел.

# Программа получает из stdin натуральное число n. Затем получает из stdin по очереди n целых чисел.
# Сумму положительных чисел из введённых программа выводит в stdout.

# Пример ввода:
#     6
#     3
#     -5
#     1
#     10
#     -1
#     8

# Пример вывода:
#     22


number_list = []

while True:
    num = int(input('Ведите число положительное число или 0 что бы закончить ввод: '))
    if num >= 0:
        number_list.append(num) 
    if num == 0:
        break
print(sum(number_list))


# Комментарии преподавателя:
# Всё верно.