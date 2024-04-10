# Написать программу, которая подсчитывает стоимость отправки телеграммы.

# В прошлом веке для отправки коротких текстовых сообщений люди использовали телеграммы. В разное время их стоимость рассчитывалась по-разному. Но при передаче телеграмм по ключу (морзянкой) стоимость отправки телеграммы # зависит от количества знаков. 
# В нашей задаче примем, что один символ буквы или цифры стоит тридцать копеек.

# Программа получает из stdin строку с текстом телеграммы.
# Программа выводит в stdout стоимость в рублях и копейках, согласно формату в примере ниже.

# Пример ввода:
#     грузите апельсины бочках братья карамазовы

# Пример вывода:
#     11 руб. 40 коп.

text = input('Введите текст: ')
count = len(text.replace(" ", ""))
print(count)
rub = count * 30 // 100
cop = count * 30 - (rub * 100)

print(f'Цена за текст составляет: {rub} рублей {cop} копеек')
# Введите текст: грузите апельсины бочках братья карамазовы
# 38
# Цена за текст составляет: 11 рублей 40 копеек