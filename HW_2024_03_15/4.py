
# Написать программу, которая осуществляет поиск в словаре по значению.

# Программа в цикле получает из stdin число и строку, разделённые пробелом (цикл прерывается при вводе пустой строки). Из полученных пар формируется словарь. 
#     Например, это может быть словарь, задающий соответствие между кодами и названиями ошибок сервера базы данных (см. примеры ввода).
# После завершения работы цикла программа получает из stdin строку — одно из введённых ранее значений.

# Программа выводит в stdout ключ, соответствующий введённому значению. Если введённое значение отсутствует в словаре (маловероятный сценарий), то программа выводит текст "! value error !".

# Пример ввода 1:
#     1004 ER_CANT_CREATE_FILE
#     1005 ER_CANT_CREATE_TABLE
#     1006 ER_CANT_CREATE_DB
#     1007 ER_DB_CREATE_EXISTS
#     1008 ER_DB_DROP_EXISTS
#     1010 ER_DB_DROP_RMDIR
#     1016 ER_CANT_OPEN_FILE
#     1022 ER_DUP_KEY
    
#     ER_CANT_CREATE_DB

# Пример вывода 1:
#     1006

# Пример ввода 2:
#     4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
#     4108 ER_GIPK_COLUMN_EXISTS
#     4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
#     4113 ER_DA_EXPIRE_LOGS_DAYS_IGNORED
#     4114 ER_CTE_RECURSIVE_NOT_UNION
    
#     ER_CANT_OPEN_FILE

# Пример вывода 2:
#     ! value error !



# # Создаем пустой словарь
# dictionary = {}

# # Цикл получения пар чисел и строк
# while True:
#     input_str = input()
#     if input_str == "":
#         break
#     key, value = input_str.split()
#     dictionary[value] = key

# # Получаем значение для поиска
# search_value = input()

# # Поиск значения в словаре и вывод соответствующего ключа
# if search_value in dictionary:
#     print(dictionary[search_value])
# else:
#     print("! value error !")

dictionary = {}
while True:
    try:
        pair = input().split()
        if len(pair) == 0:
            break
        dictionary[pair[1]] = pair[0]
    except:
        break

search_value = input()

if search_value in dictionary:
    print(dictionary[search_value])
else:
    print("! value error !")


# Комментарий преподавателя:

# Использование блока try-except:
# В данном случае блок try-except не нужен.
# Лучше проверить длину введенной пары и обработать
# ввод корректно без использования исключений.

# Использовать if not pair:
# вместо if len(pair) == 0: для проверки пустой строки.