# core/entities/person.py
class Person:
    def __init__(self, id_number, name, last_name, phone_number):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.id_number = id_number
