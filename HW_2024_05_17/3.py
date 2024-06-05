class Publisher:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_info(self):
        print(f"Издательство {self.name}, расположенное в {self.location}")

    def publish(self, message):
        print(f"Печатаем {message} в издательстве {self.name} ({self.location})")


class BookPublisher(Publisher):
    def __init__(self, name, location, num_authors):
        super().__init__(name, location)
        self.num_authors = num_authors

    def publish(self, message, author):
        print(f"Передаем рукопись '{message}', написанную автором {author} в издательство {self.name} ({self.location})")


class NewspaperPublisher(Publisher):
    def __init__(self, name, location, num_pages):
        super().__init__(name, location)
        self.num_pages = num_pages

    def publish(self, message):
        print(f"Печатаем свежий номер со статьей '{message}' на главной странице в издательстве {self.name} ({self.location})")


publisher = Publisher("АБВГД Пресс", "Москва")
publisher.publish("Справочник писателя")

book_publisher = BookPublisher("Важные Книги", "Самара", 52)
book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
newspaper_publisher.publish("Новая версия Midjourney будет платной")