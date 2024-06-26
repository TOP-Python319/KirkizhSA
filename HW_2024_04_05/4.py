
# Напишите программу, записывающую в текстовый файл random.txt 
# 25
# 25 случайных чисел в диапазоне от 
# 111
# 111 до 
# 777
# 777 (включительно), каждое с новой строки.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна создать файл с именем random.txt и записать в него случайные числа в соответствии с условием задачи.

# Примечание 1. Исполняемая программа и указанный файл находятся в одной папке.
# Примечание 2. Для генерации случайных чисел используйте модуль random.

import random

with open("random.txt", "w") as file:
    for r in range(25):
        random_num = random.randint(111, 777)
        file.write(str(random_num) + "\n")

# всё верно