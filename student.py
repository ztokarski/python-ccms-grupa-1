import user from user.py
import attendace from attendace.py
import submissions from submissions.py

class Student(User):

def __init__(self,name, surname, age, gender, pesel, login, password, date_removed, status, class_attendance, grades, submissions):
    User.__init__(name, surname, age, gender, pesel, login, password, date_removed, status)
    # self.class_attendance = class_attendance(self)
    # self.grades = grades(self)
    # self.submissions = submissions(self)
