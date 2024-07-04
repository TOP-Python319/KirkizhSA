class DictMixin:
    """
    Миксин для преобразования объектов в словарь.
    """

    def to_dict(self):
        """
        Преобразует объект в словарь.
        """
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (DictMixin, list)):
                result[key] = self.convert_to_dict(value)
            else:
                result[key] = value
        return result

    def convert_to_dict(self, value):
        """
        Вспомогательный метод для рекурсивного преобразования
        объектов в словарь.
        """
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, list):
            return [self.convert_to_dict(item) for item in value]
        else:
            return value

class Phone(DictMixin):
    def __init__(self, number):
        self.number = number


class Person(DictMixin):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Address(DictMixin):
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Company(DictMixin):
    def __init__(self, name, address):
        self.name = name
        self.address = address


address = Address("123 Main St", "Anytown", "CA", "12345")
john_doe = Person("John Doe", 30, address)

john_doe_dict = john_doe.to_dict()

assert john_doe_dict == {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip_code': '12345'
    }
}

address = Address("123 Main St", "Albuquerque", "NM", "987654")
assert address.to_dict() == {
    'street': '123 Main St',
    'city': 'Albuquerque',
    'state': 'NM',
    'zip_code': '987654'
}
walter = Person("Walter White", 30, address)
assert walter.to_dict() == {'address': {'city': 'Albuquerque',
                                        'state': 'NM',
                                        'street': '123 Main St',
                                        'zip_code': '987654'},
                            'age': 30,
                            'name': 'Walter White'}

walter_phone = Phone("555-1234")
walter.phone = walter_phone
assert walter.to_dict() == {'address': {'city': 'Albuquerque',
                                        'state': 'NM',
                                        'street': '123 Main St',
                                        'zip_code': '987654'},
                            'age': 30,
                            'name': 'Walter White',
                            'phone': {'number': '555-1234'}}

company_address = Address("3828 Piermont Dr", "Albuquerque", "NM", "12345")
company = Company("SCHOOL", company_address)

assert company.to_dict() == {'address': {'city': 'Albuquerque',
                                         'state': 'NM',
                                         'street': '3828 Piermont Dr',
                                         'zip_code': '12345'},
                             'name': 'SCHOOL'}

jesse_address = Address("456 Oak St", "Albuquerque", "NM", "12345")
jesse = Person("Jesse Bruce Pinkman", 27, jesse_address)
jesse.phone = Phone("555-5678")

fring = Person("Gustavo Fring", 55, Address("Los Pollos Hermanos", "Albuquerque", "NM", "12345"))
fring.friends = [walter, jesse]

assert fring.to_dict() == {'address': {'city': 'Albuquerque',
                                       'state': 'NM',
                                       'street': 'Los Pollos Hermanos',
                                       'zip_code': '12345'},
                           'age': 55,
                           'friends': [{'address': {'city': 'Albuquerque',
                                                    'state': 'NM',
                                                    'street': '123 Main St',
                                                    'zip_code': '987654'},
                                        'age': 30,
                                        'name': 'Walter White',
                                        'phone': {'number': '555-1234'}},
                                       {'address': {'city': 'Albuquerque',
                                                    'state': 'NM',
                                                    'street': '456 Oak St',
                                                    'zip_code': '12345'},
                                        'age': 27,
                                        'name': 'Jesse Bruce Pinkman',
                                        'phone': {'number': '555-5678'}}],
                           'name': 'Gustavo Fring'}

print('Good')


# Комментарии преподавателя:

# 1. Решение задачи в целом верно и соответствует условию.
# 2. Миксин DictMixin реализован правильно и предоставляет необходимый функционал для преобразования объектов в словари.
# 3. Классы Phone, Person, Address и Company наследуют миксин DictMixin и реализуют необходимые конструкторы для создания объектов.
# 4. Метод to_dict() реализован правильно и предоставляет корректное представление объекта в виде словаря.
# 5. Вспомогательный метод convert_to_dict() используется для рекурсивного преобразования вложенных объектов и списков.

# Что можно улучшить:
# 1. Отсутствует проверка типов атрибутов. Это может привести к ошибкам при преобразовании объектов в словари, если атрибуты имеют неверные типы данных.
# Для устранения этой проблемы можно добавить проверку типов атрибутов в конструкторах классов.
# 2. В методе to_dict() можно добавить сортировку атрибутов по ключам,
# чтобы гарантировать одинаковый порядок атрибутов в словаре при преобразовании разных объектов одного класса.
# 3. В методе to_dict() можно предусмотреть возможность настраивать формат представления объекта в виде словаря, например,
# предоставить возможность указывать какие-то дополнительные параметры для форматирования.
# 5. В коде можно добавить комментарии, чтобы облегчить его понимание другим разработчикам.