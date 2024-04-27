# Завдання 3
# Створіть клас для конвертування з метричної системи в
# англійську, та навпаки. Реалізуйте функціональність у вигляді
# статичних методів. Обов’язково реалізуйте конвертування
# заходів довжини.
class UnitConverter:
    @staticmethod
    def meters_to_feet(meters):
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet):
        return feet / 3.28084

meters_length = 10
feet_length = UnitConverter.meters_to_feet(meters_length)
print(f"{meters_length} метрів = {feet_length} футів")

converted_back = UnitConverter.feet_to_meters(feet_length)
print(f"{feet_length} футів = {converted_back} метрів")


#class Bank:
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