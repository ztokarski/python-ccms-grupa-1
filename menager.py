import Person from person.py

class Menager(Employee):


def __init__(self,name, surname, age, gender, pesel, login, password, date_addeed, date_remove, status):
    Employee.__init__(name, surname, age, gender, pesel, login, password, date_addeed, date_remove, status)

def viev_student_details():
    pass

def add_mentor():
    pass

def remove_mentor():
    pass

def viev_mentors():
    pass
            
@classmethod

def get_all():
    pass
