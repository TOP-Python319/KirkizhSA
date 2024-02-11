""" ==========  4  ==========

Написать программу, которая сравнивает две клетки шахматной доски.

Программа должна по очереди получить из stdin координаты двух клеток шахматной доски (см. пример ввода).
    По горизонтали клетка кодируется латинскими буквами от ‘a’ до ‘h’.
    По вертикали клетка кодируется цифрами от 1 до 8.

Если две заданные клетки покрашены в один цвет, то программа должна вывести в stdout слово “да”. Если клетки покрашены в разные цвета, то должно быть выведено слово “нет”.

Примечание: в традиционных шахматах клетка а1 всегда чёрного цвета.

Пример ввода:
    a1
    b2

Пример вывода:
    да
 """
cell1 = input("Введите координаты первой клетки: ")
cell2 = input("Введите координаты второй клетки: ")
col1 = ord(cell1[0]) - ord('a') + 1  # 103 - 97 + 1 = 7 
row1 = int(cell1[1])                 # 5   
col2 = ord(cell2[0]) - ord('a') + 1  # 104 - 97 + 1 = 8
row2 = int(cell2[1])                 # 6
if (col1 + row1) % 2 == (col2 + row2) % 2:     # (7 + 5) % 2  = (8 + 6) % 2  0 = 0 (да)
    print('да') 
else:
    print('нет')
"""
Введите координаты первой клетки: g5
Введите координаты второй клетки: h6
да


Введите координаты первой клетки: a3
Введите координаты второй клетки: f5
нет
"""