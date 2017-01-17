import User from user.py


class Employee(User):

def __init__(self,name, surname, age, gender, pesel, login, password, date_addeed, date_remove, status):
    User.__init__(name, surname, age, gender, pesel, login, password, date_addeed, date_remove, status)

def viev_student_details():
    pass

def create_employee():
    pass

@classmethod

def get_all():
    pass
