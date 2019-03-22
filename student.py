import datetime


class Student:
    def __init__(self, surname, name, birthday):
        self.surname = surname
        self.name = name
        self.birthday = birthday

    def age(self):
        current_year = datetime.datetime.now().year

        return current_year - self.birthday
