# Написать программу, которая подсчитывает количество очков за слово в настольной игре "Эрудит".

# Программа получает из stdin строку, содержащую одно слово на русском языке.

# Используя заранее составленный словарь программа вычисляет количество очков, которое должно быть начислено за введённое слово.
#     Воспользуйтесь словарём из приложенного к заданию файла # ref 5.py

# Программа выводит в stdout число.

# Подумайте о способах оптимизации программы.

# Примечание: согласно правилам большинства версий "Эрудита" буквы 'е' и 'ё' взаимозаменяемы.

# Пример ввода:
#     синхрофазотрон

# Пример вывода:
#     29

scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

def callculation_score(word):
    score = 0
    for letter in word.upper():
        for key, value in scores_letters.items():
            if letter in value:
                score += key
    return score


word = input().replace('Ё', 'Е')
print(callculation_score(word))


# синхрофазотрон
# 29
# ЖЗХЦЧ
# 25

# Комментарий преподавателя:
# всё верно! =)