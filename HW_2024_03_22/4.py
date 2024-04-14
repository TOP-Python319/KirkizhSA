# Написать функцию с именем countable_nouns, которая возвращает существительное русского языка, согласованное с числом.

# Функция принимает обязательными аргументами целое число и кортеж с вариантами согласования существительного (см. пример проверки).
    
#     Первый аргумент должен быть передан в виде объекта int.
    
#     Согласно правилам русского языка о согласовании составных количественных числительных и существительных, возможны три варианта согласования. Поэтому кортеж, передаваемый вторым аргументом, должен содержать ровно три объекта str.
#         В отличие от списков, элементы кортежа аннотируются каждый по отдельности. Таким образом, кортеж из трёх строк должен быть аннотирован как tuple[str, str, str]

# Функция возвращает одно слово из трёх, переданных вторым аргументом, которое согласуется с переданным первым аргументом числом.

# С числительными из каждого числового ряда согласуется одна форма существительного или отдельное существительное:
#     1, 21, 31 ... 451 ...
#     2, 3, 4, 22, 23, 24 ... 342, 343, 344 ...
#     0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27, 28, 29, 30, 35 ... 675, 676 ...

# Написанную функцию необходимо протестировать вручную.
# Пример ручного теста:
#     >>> countable_nouns(1, ("год", "года", "лет"))
#     'год'
#     >>> countable_nouns(2, ("год", "года", "лет"))
#     'года'
#     >>> countable_nouns(10, ("год", "года", "лет"))
#     'лет'
#     >>> countable_nouns(12, ("год", "года", "лет"))
#     'лет'
#     >>> countable_nouns(22, ("год", "года", "лет"))
#     'года'


def countable_nouns(number: int, forms: tuple[str, str, str]) -> str:
    if number % 10 == 1 and number % 100 != 11:
        return forms[0]
    elif 2 <= number % 10 <= 4 and (number % 100 < 10 or number % 100 >= 20):
        return forms[1]
    else:
        return forms[2]
    
print(countable_nouns(1, ("год", "года", "лет")))  # 'год'
print(countable_nouns(2, ("год", "года", "лет")))  # 'года'
print(countable_nouns(10, ("год", "года", "лет")))  # 'лет'
print(countable_nouns(12, ("год", "года", "лет")))  # 'лет'
print(countable_nouns(22, ("год", "года", "лет")))  # 'года'

# год
# года
# лет
# лет
# года