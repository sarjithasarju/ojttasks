import re

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer.")
        self._age = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if not self.is_valid_email(value):
            raise ValueError("Invalid email format.")
        self._email = value

    @staticmethod
    def is_valid_email(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None


try:
    person = Person(name="John Doe", age=30, email="john.doe@example.com")
    print(f"Name: {person.name}, Age: {person.age}, Email: {person.email}")

    
except ValueError as e:
    print(e)
