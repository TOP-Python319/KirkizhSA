# Ваша задача реализовать класс Stack, у которого есть:

#   метод __init__() создаёт новый пустой стек. 
#     Параметры данный метод не принимает.
#     Создает атрибут экземпляра values, 
#     где будут в дальнейшем храниться элементы стека в виде списка (list), 
#     изначально при инициализации задайте значение атрибуту values, равное пустому списку;
 
#   метод push(item) добавляет новый элемент на вершину стека, метод ничего не возвращает;
 
#   метод pop() удаляет верхний элемент из стека.
#     Параметры не требуются, метод возвращает элемент.
#     Стек изменяется.
#     Если пытаемся удалить элемент из пустого списка, 
#     необходимо вывести сообщение "Empty Stack";
 
#   метод peek() возвращает верхний элемент стека, но не удаляет его.
#     Параметры не требуются, стек не модифицируется.
#     Если элементов в стеке нет, 
#     распечатайте сообщение "Empty Stack",
#     верните None после этого;
 
#   метод is_empty() проверяет стек на пустоту.
#     Параметры не требуются, возвращает булево значение.
 
#   метод size() возвращает количество элементов в стеке.
#     Параметры не требуются, тип результата — целое число.


class Stack:
    def __init__(self) -> None: #создаёт новый пустой стек. 
        self.values = []

    def push(self, item): #добавляет новый элемент на вершину стека, метод ничего не возвращает;
        self.values.append(item)
    
    def pop(self): #метод pop() удаляет верхний элемент из стека.
        if len(self.values) == 0:
            print('Empty Stack')
        else:
            return self.values.pop()
    
    def peek(self): #возвращает верхний элемент стека, но не удаляет его.
        if len(self.values) == 0:
            print('Empty Stack')
            return None
        else:
            return self.values[-1]
    
    def is_empty(self): #проверяет стек на пустоту.
        return len(self.values) == 0
    
    def size(self): #возвращает количество элементов в стеке.
        return len(self.values)
stack = Stack()
stack.push(10)
stack.push(12)
stack.push(14)
stack.size()

# >>> stack.push(10)
# >>> stack.is_empty()
# False
# >>> stack.size()
# 4
# >>> stack.is_empty()
# False
# >>> stack.peek()
# 10
# >>> stack.pop()
# 10
# >>>
# >>> stack.size()
# 3
# >>> stack.pop()
# 14
# >>> stack.pop()
# 12
# >>> stack.pop()
# 10
# >>> stack.pop()
# Empti Stack
# >>> stack.peek()
# Empti Stack
# >>> stack.size()
# 0
# >>> stack.is_empty()
# True
# >>>

# Комментарий преподаваеля:
# Хорошее решение, у меня есть пару замечаний:

# В сообщениях "Empti Stack" должно быть "Empty Stack".
# Аннотации типов помогают понять, какие типы данных ожидаются и возвращаются
# методами класса. Это делает код более понятным и помогает при разработке и отладке.

# Методы pop() и peek() можно упростить,
# используя метод is_empty() для проверки стека на пустоту.
# Это делает код более читаемым.