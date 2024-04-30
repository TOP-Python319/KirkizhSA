# Вам доступен текстовый файл text.txt с одной строкой текста. Напишите программу, которая выводит на экран эту строку в обратном порядке.

# Формат входных данных
# На вход программе ничего не подается.

# Формат выходных данных
# Программа должна вывести строку указанного файла в обратном порядке.

# Примечание 1. Исполняемая программа и указанный файл находятся в одной папке.
# Примечание 2. Используйте менеджер контекста.

with open("text.txt", "r", encoding='UTF-8') as text:
    contents = text.read()
    reversed_contents = contents[::-1]
    print(reversed_contents)

#.enil hcae fo rettel tsrif eht tuo tnirp dna txt.egassem_terces daeR 

with open("text.txt", "r", encoding='UTF-8') as text:
    contents = text.read()
    dict_contens = contents.split()
    reversed_contents = dict_contens.copy()
    reversed_contents.reverse() 
    my_string = ' '.join(reversed_contents)          
    print(my_string)

#line. each of letter first the out print and secret_message.txt Read   