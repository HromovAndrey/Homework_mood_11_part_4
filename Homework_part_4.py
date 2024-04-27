# Завдання 1
# До вже реалізованого класу «Дріб» додайте
# статичний метод, який при виклику
# повертає кількість створених об’єктів
# класу «Дріб
class Fraction:
    instance_count = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.instance_count += 1

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    @staticmethod
    def get_instance_count():
        return Fraction.instance_count

fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

fraction3 = Fraction(2, 3)

print(Fraction.get_instance_count())
print(fraction1)
print(fraction2)

