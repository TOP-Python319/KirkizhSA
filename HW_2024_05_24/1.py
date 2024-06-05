class Money:
    def __init__(self, dollars, cents) -> None:
        self.dollars = dollars
        self.cents = cents
        self.total_cents = '' 

    def get_dollars(self) -> int:
        return self.dollars
    
    def set_dollars(self) -> int:
        if self.dollars >= 0:
            return self.dollars 
        else:
            print("Error dollars")

    def get_cents(self) -> int:
        return self.cents

    def set_cents(self) -> int:
        if 0 <= self.cents < 100:
            self.total_cents = self.dollars * 100 + self.cents
        else:
            print("Error cents")

    def __str__(self) -> str:
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"
Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents) # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов

# Ваше состояние составляет 101 долларов 99 центов
# 101 99
# 10199
# Ваше состояние составляет 666 долларов 99 центов
# Ваше состояние составляет 666 долларов 12 центов