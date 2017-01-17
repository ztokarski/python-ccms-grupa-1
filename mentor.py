import employee from employee.py
import attendace from attendace.py
import submissions from submissions.py


class Mentor(Employee):


def __init__(self,name, surname, age, gender, pesel, login, password, date_addeed, date_remove, status, class_attendance, grades, submissions):
    Employee.__init__(name, surname, age, gender, pesel, login, password, date_addeed, date_remove, status)

def create_mentor():
    pass

def make_assigment():
    pass

def grade_subbmission():
    pass

def check_attendance():
    pass

@classmethod

def get_all():
    pass
