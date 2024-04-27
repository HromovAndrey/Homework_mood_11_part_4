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
            print(f"Користувача з ім'ям {username} не існує. Спочатку додайте користувача.")

    @classmethod
    def add_users_and_contacts(cls, users_and_contacts):
        info_system = cls()
        for user, contacts in users_and_contacts.items():
            info_system.add_user(user)
            for contact in contacts:
                info_system.add_contact(user, contact)
        return info_system

users_and_contacts = {
    "user1": ["contact1", "contact2"],
    "user2": ["contact3", "contact4"],
}

info_system = InformationSystem.add_users_and_contacts(users_and_contacts)

print(info_system.data)


