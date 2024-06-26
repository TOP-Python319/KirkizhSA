# Написать программу, которая требуемое количество чисел последовательности Фибоначчи.
# 
# Программа получает из stdin натуральное число n. 
# Далее, программа считает и выводит в stdout n чисел последовательности Фибоначчи.

# Примечание: последовательность Фибоначчи — это последовательность натуральных чисел, которая начинается с двух единиц, а каждое # последующее число является суммой двух предыдущих: 1, 1, 2, 3, 5, 8, 13, …

# Пример ввода 1:
#     1

# Пример вывода 1:
#     1

# Пример ввода 2:
 #    17


n = int(input('Введите натуральное число: '))

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_seq = [1, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        return fib_seq

fib_list = fibonacci(n)
print(" ".join(map(str, fib_list)))



# Введите натуральное число: 6
# 1 1 2 3 5 8   


# Комментарий преподавателя:
# Всё верно