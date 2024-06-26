# Написать программу, которая проверяет, является ли один список частью другого списка.

# Программа два раза получает из stdin произвольное количество целых чисел, разделённых пробелом. Из каждого ввода формируется отдельный список объектов int.

# Далее, программа определяет, можно ли из первого списка выбрать срез с шагом по умолчанию (единица) так, чтобы получился второй список.
#     В решении не обязательно использовать именно срезы, есть много разных способов.

# Программа выводит в stdout текстовый ответ.

# Примечание: пустой список является частью любого списка, включая пустой.

# Пример ввода 1:
#     1 2 3 4
#     1 2

# Пример вывода 1:
#     да

# Пример ввода 2:
#     1 2 3 4
#     2 4

# Пример вывода 2:
#     нет


# Считываем два списка из stdin
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# Проверяем, является ли list2 частью list1
def is_subset(lst1, lst2):
    if not lst2:
        return True
    for i in range(len(lst1) - len(lst2) + 1):
        if lst1[i:i+len(lst2)] == lst2:
            return True
    return False

if is_subset(list1, list2):
    print("да")
else:
    print("нет")


# Комментарий преподавателя:
# Логика проверки подсписка корректна.
# Использование срезов и цикла обеспечивает правильную проверку
# наличия lst2 в lst1.