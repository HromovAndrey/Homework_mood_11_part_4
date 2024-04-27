# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print(f"Hello my name is {self.name} and i am {self.age} years old")
#     def celebrate_birthday(self):
#         self.age += 1
#         print(f"Happy birthday! Now i am {self.age} year old")
#
# person = Person("Andrii", 27)
# person.greet()
# person.celebrate_birthday()
# result = Person.greet(person)

# class Bank:
#     def __init__(self):
#         self.balance = 10
#
#     @staticmethod
#     def uah_to_usd(value_usd):
#         return value_usd / 38
#
# object = Bank()
# print(object.uah_to_usd(100))
# print(Bank.uah_to_usd(2000))

# class Calcylator:
#     x = 4
#     @staticmethod
#     def add(y):
#         return Calcylator.x + y
#
#
# print(Calcylator.add(5))

# class Bank:
#     count = 0
#     exchange_rate_usd_uah = 38
#     def __init__(self):
#         Bank.count += 1
#         self.balance = 10
#     @staticmethod
#     def uah_to_usd(value_uah):
#         print(Bank.exchange_rate_usd_uah)
#         return value_uah / 38
#
#     @classmethod
#     def uah_to_usd2(cls, value_uah):
#         return value_uah / cls.exchange_rate_usd_uah
#
#     def set_balance(self, balance):
#         self.balance = balance
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#     @classmethod
#     def get_exchange_rate(cls):
#         return cls.exchange_rate_usd_uah
#
# object = Bank()
# print(object.uah_t


# class Person:
#     count = 0
#     def __init__(self, name):
#         self.name = name
#         Person.count += 1
#
#     @classmethod
#     def get_count(cls):
#         return cls.count
#
#     def bonus (self, x = 10):
#         return Person.get_count() + 10
#
# p1 = Person("Stive")
# p2 = Person("Oleg")
# print(Person.get_count())
# print(p1.bonus())

class Calculator:
    @staticmethod
    def add_numbers(num1, num2 ):
        return num1 + num2
    @classmethod
    def add_numbers_with_round(cls, num1, num2):
        num1 = round(num1)
        num2 = round(num2)
        return cls.add_numbers(num1, num2)
