import math

# """ 
#   ==========  2  ==========  

# Написать функцию с именем taxi_cost, которая вычисляет стоимость поездки на такси.

# Функция принимает обязательным аргументом длину маршрута в метрах и необязательным аргументом длительность ожидания в минутах.
    
#     Оба аргумента должны быть позиционно-ключевыми и переданы в виде объектов int.
    
#     Значение по умолчанию для длительности ожидания — ноль.

# Функция возвращает стоимость поездки или None, если вычисление невозможно.
    
#     Переданные длина маршрута и длительность ожидания могут быть нулями или положительными числами, но не должны быть отрицательными числами. 
#     Если всё же функции были явно переданы отрицательные числа, то это означает невозможность корректно провести вычисление.
    
#     Если вычисление возможно, то возвращается объект int.
#         Аннотация нескольких типов записывается с помощью |
#         >>> def func() -> int | None:
#         ...     pass

# Расчёт стоимости осуществляется по следующим правилам:
#     - базовая стоимость поездки 80 рублей
#     - за каждые 150 метров к стоимости добавляется 6 рублей
#     - за каждую минуту ожидания к стоимости добавляется 3 рубля
#     - при отмене поездки (длина маршрута составила 0 метров) к стоимости добавляется штраф 80 рублей и стоимость времени ожидания
#     - итоговая стоимость математически округляется до целого числа

# Написанную функцию необходимо протестировать вручную.
# Пример ручного теста:
#     >>> taxi_cost(1500)
#     140
#     >>> taxi_cost(2560)
#     182
#     >>> taxi_cost(0, 5)
#     175
#     >>> taxi_cost(42130, 8)
#     1789
#     >>> print(taxi_cost(-300))
#     None
# """


def taxi_cost(route_length: int, waiting_time: int = 0) -> int | None:
    if route_length >= 0 and waiting_time >= 0: # если длина маршрута и время ожидания >= 0
        base_cost = 80
        cost_per_meter = 6
        cost_per_minute = 3
        
        if route_length == 0: # если длина маршрута = 0
            penalty = 80 + waiting_time * cost_per_minute # штраф 80 + время * стоимость времени ожидания
            return base_cost + penalty
        
        route_cost = base_cost + math.ceil(route_length / 150) * cost_per_meter
        waiting_cost = waiting_time * cost_per_minute
        
        return math.ceil(route_cost + waiting_cost)
    else:
        return None
    
    
r  = taxi_cost(1500)
print(r)
# 140