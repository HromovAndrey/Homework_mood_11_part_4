# Завдання 4
#  Створіть клас InformationSystem, який має атрибут data
# - словник, де ключі - це імена користувачів, а значення -
# список їх контактів. Реалізуйте методи класу для додавання
# нових користувачів та їх контактів.

class InformationSystem:
    def __init__(self):
        self.data = {}

    def add_user(self, username):
        if username not in self.data:
            self.data[username] = []

    def add_contact(self, username, contact):
        if username in self.data:
            self.data[username].append(contact)
        else:
            print(f"Користувача з ім'ям {username} не існує.")

    @classmethod
    def class_method(cls, x):
        return cls.class_variable * x

# Приклад використання класу
info_system = InformationSystem()

# Додаємо нових користувачів та їх контакти
info_system.add_user("user1")
info_system.add_contact("user1", "contact1")
info_system.add_contact("user1", "contact2")

info_system.add_user("user2")
info_system.add_contact("user2", "contact3")
info_system.add_contact("user2", "contact4")

# Виводимо дані системи
print(info_system.data)