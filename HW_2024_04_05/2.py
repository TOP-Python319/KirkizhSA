#2
# Вам доступен текстовый файл data.txt, в котором записаны строки текста. Напишите программу, выводящую все строки данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести строки указанного файла в обратном порядке, каждую на новой строке.

# Примечание 1. Исполняемая программа и указанный файл находятся в одной папке.
# Примечание 2. Используйте менеджер контекста.
# Примечание 3. Получить список всех строк файла можно при помощи метода readlines().
# Примечание 4. Не забывайте про символ конца строки '\n'.

with open("data.txt", "r", encoding="utf-8") as data:
    contents = data.readlines()

    for line in reversed(contents):
        print(line.strip())
    
    
    # del_contens = contents.reple

# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
