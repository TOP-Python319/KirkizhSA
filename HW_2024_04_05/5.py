# Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи содержимого этого файла в файл output.txt 
# в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел. Нумерация строк должна начинаться с 1.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна создать файл с именем output.txt и записать в него пронумерованные строки файла input.txt.

# Примечание 1. Исполняемая программа и указанные файлы находятся в одной папке.
# Примечание 2. Используйте встроенную функцию enumerate().
# Примечание 3. Если бы файл input.txt содержал строки:

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

# то файл output.txt имел бы вид:
# 1) Beautiful is better than ugly.
# 2) Explicit is better than implicit.
# 3) Simple is better than complex.
# 4) Complex is better than complicated.

# ###

with open('input.txt', 'r') as file:
    lines = file.readlines()

with open('output.txt', 'w') as file:
    for index, line in enumerate(lines, start=1):
        file.write(f"{index}) {line}")
