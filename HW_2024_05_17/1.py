class Publisher():
    def __init__(self, name, location):
        self.name = name
        self.location = location
   
    def get_info(self):
        ...  # зачем он нужен???
   
 
    def publish(self, message):
        self.message = message
        print(f"Готовим '{self.message}' к публикации в {self.name} ({self.location})")
 
class BookPublisher(Publisher):
    def __init__(self, name, location, num_authors):
        super().__init__(name, location)
        self.num_authors = num_authors
       
 
    def publish(self, message, author):
        self.message = message
        self.author = author
        print(f"Передаем рукопись '{self.message}', написанную автором {self.author} в издательство {self.name} ({self.location})")
 
class NewspaperPublisher(Publisher):
    def __init__(self, name, location, num_pages):
        super().__init__(name, location)
        self.num_pages = num_pages
   
 
 
    def publish(self, message):
        self.message = message
        print(f"Печатаем свежий номер со статьей '{self.message}' на главной странице в издательстве {self.name} ({self.location})")
 
publisher = Publisher("АБВГД Пресс", "Москва")
publisher.publish("Справочник писателя")
 
book_publisher = BookPublisher("Важные Книги", "Самара", 52)
book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")
 
newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
newspaper_publisher.publish("Новая версия Midjourney будет платной")
 
# Готовим 'Справочник писателя' к публикации в АБВГД Пресс (Москва)
# Передаем рукопись 'Приключения Чебурашки', написанную автором В.И. Пупкин в издательство Важные Книги (Самара)
# Печатаем свежий номер со статьей 'Новая версия Midjourney будет платной' на главной странице в издательстве Московские вести (Москва)


# Комментарий преподавателя:

# 1. Правильно реализовано наследование с созданием суперкласса Publisher и двух подклассов BookPublisher и NewspaperPublisher.
# 2. Использован метод super().__init__(name, location) для вызова конструктора суперкласса и инициализации атрибутов name и location.
# 3. Реализация метода publish() в подклассах соответствует примерам использования.
# 4. Код работает корректно и выводит результаты, как указано в примерах.

# Что можно улучшить:
# Метод get_info(self) в суперклассе Publisher не реализован.
# Метод нужен для предоставления информации о названии и расположении издательства.
# Например:
# def get_info(self):
#     return f"{self.name} ({self.location})"

# В целом, хорошо выполненная работа. =)