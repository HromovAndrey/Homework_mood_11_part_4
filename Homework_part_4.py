# Завдання 2
# Створіть клас для конвертування температури з Цельсія
# у Фаренгейт, і навпаки. У класі має знаходитися два статичні
# методи: для конвертування з Цельсія у Фаренгейт і для конвертування з Фаренгейта у Цельсій. Також клас має розрахувати
# кількість підрахунків температури та повернути це значення
# статичним методом.

class TemperatureConverter:
    conversion_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.conversion_count += 1
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.conversion_count += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def get_conversion_count():
        return TemperatureConverter.conversion_count

celsius_temp = 25
fahrenheit_temp = TemperatureConverter.celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp} градусів Цельсія = {fahrenheit_temp} градусів Фаренгейта")

converted_back = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
print(f"{fahrenheit_temp} градусів Фаренгейта = {converted_back} градусів Цельсія")

print(f"Кількість конвертацій: {TemperatureConverter.get_conversion_count()}")
