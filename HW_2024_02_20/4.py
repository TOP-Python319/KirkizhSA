#Написать программу, которая подсчитывает количество простых чисел среди всех чисел одной разрядности.

#Программа получает из stdin натуральное число n — количество разрядов.
#Далее, с помощью вложенных циклов программа считает количество простых чисел среди всех n-значных чисел.
#Результат программа выводит в stdout.

#Примечание: простые числа делятся только на единицу и на само себя.

#Подсказка: конкатенация последовательностей может быть осуществлена посредством умножения на число:
#    >>> 'z' * 4
#    'zzzz'

#Пример ввода:
#    3

#Пример вывода:
#    143
n = int(input())
end_number = int('1' + '0' * n)
# print(f'end_number = {end_number}')
start_number = end_number // 10
# print(f'start_number = {start_number}')
count = 0
for num in range(start_number, end_number):
    for div in range(2, num):
        if num % div == 0:
            #print(f'div = {div}')
            #print(f'num = {num}')
            break
        elif num % div != 0 and div == num - 1:
            count += 1
print(count)   