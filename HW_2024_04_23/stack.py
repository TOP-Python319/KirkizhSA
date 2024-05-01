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
    def __init__(self) -> None:
        self.values = []

    def push(self, item):
        self.values.append(item)
    
    def pop(self):
        if len(self.values) == 0:
            print('Empti Stack')
        else:
            return self.values.pop()
    
    def peek(self):
        if len(self.values) == 0:
            print('Empti Stack')
            return None
        else:
            return self.values[-1]
    
    def is_empty(self):
        return len(self.values) == 0
    
    def size(self):
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