import sys
from student import *
from user import *
from assigment import *
from attendance import *
from mentor import *
from menager import *
from UI import *
from employee import *
import time


date = time.localtime()
actual_date = "{}/{}/{}".format(date[0],date[1],date[2])


# def clearing_duplicates_student_assignment_loading_data():
#
#     Assignment.loading_file()
#     Student.loading_file("students2.csv")
#     assignments_submitted = []
#
#     for student in Student.get_all():
#         for submission in student.submissions.submissions_list:
#             assignments_submitted.append(submission.assignment.name_assignment)
#
#     print(assignments_submitted)
#
#     no_duplicate_assignments = []
#     for assignment in Assignment.get_all():
#         if assignment.name_assignment in assignments_submitted:
#             assignments_submitted.remove(assignment.name_assignment)
#
#         else:
#             no_duplicate_assignments.append(assignment)
#
#     Assignment.ASSIGNMENTS = no_duplicate_assignments


def submitting_assignment(student_obj):
    '''Viewing submitted assignments and assignments that await submission, selection options.'''

    print('Assignments to which you made submission: ')

    assignments_submitted = []

    if student_obj.submissions:
        for submission in student_obj.submissions:
            assignments_submitted.append(submission.assignment.name_assignment)

        for assignment in Assignment.get_all():
            if assignment.name_assignment in assignments_submitted:
                print(assignment)
    else:
        print('You have not made any submission to assignment.')

    print()
    print('Assignments to which submission was not made: ')
    for assignment in Assignment.get_all():

        if assignment.name_assignment not in assignments_submitted:
            print(assignment)


    assignment_to_be_submitted = input('Please give name of assignment to which you want to submit your solution: ')

    if assignment_to_be_submitted in assignments_submitted:
        student_choice = input('You have already submitted solution to this assignment. Do you want to overwrite previous submission (Yes/No)? ')
        if student_choice.lower() == 'yes':
            overwriting_submission(student_obj,assignment_to_be_submitted)

        else:
            return

    else:
        try:
            processing_submission(student_obj, assignment_to_be_submitted)

        except ValueError:
            print('There is no such assignment.')
            return




def processing_submission(student_obj, assignment_to_be_submitted):
    '''Processing submission request - creation of new instance from submission class
    and adding this instance into list of submissions in given instance of student class.'''

    for assignment in Assignment.get_all():
        if assignment.name_assignment == assignment_to_be_submitted:
            link = input('Please provide link to your solution on github: ')
            description = input('Please provide description of your solution: ')

            student_obj.submit_submission(link, description, assignment,[])
            return
    print()
    raise ValueError

def overwriting_submission(student_obj,assignment_to_be_submitted):
    '''Overwriting already made submission by replacing existing instance of submission
    class in the list of instances of submission class with new instance of submission class.'''

    for submission in range(len(student_obj.submissions)):
        if student_obj.submissions[submission].assignment.name_assignment == assignment_to_be_submitted:
            link = input('Please provide link to your solution on github: ')
            description = input('Please provide description of your solution: ')
            for assignment in Assignment.get_all():
                if assignment.name_assignment == assignment_to_be_submitted:
                    student_obj.submissions[submission] = Submission(link, description, assignment,[])
                    return


def show_grades(student_obj):
    print('Your grades: ')
    if student_obj.grades:
        for grade in student_obj.grades:
            print(grade)
        return

    else:
        print('Your submissions have not been yet assessed by Mentors.')
        return



def Password_Validator(type): #returns object

    """File loading"""
    Mentor.loading_file()
    Employee.loading_file()
    Menager.loading_file()
    Student.loading_file("students.csv")
    login = input("Login: ")
    password = input("Password: ")

    if type == "Mentor":
        Mentor.loading_file()
        for element in Mentor.get_all():
            if element.login == login:
                if element._password == password:
                    return element
    if type == "Menager":
        for element in Menager.get_all():
            if element.login == login and element.status == "active":
                if element._password == password:
                    return element

    if type == "Student":
        for element in Student.get_all():
            if element.login == login:
                if element._password == password:
                    return element

    if type == "Employee":
        for element in Mentor.get_all():
            if element.login == login:
                if element._password == password:
                    return element

def printing_start_menu():

    print("Select an option:\n"
            "1.Mentor\n"
            "2.Menager\n"
            "3.Student\n"
            "4.Employee\n"
            "5.Exit\n")

def printing_menu_mentor():

    print("1.View student list\n"
          "2.Add student\n"
          "3.Remove student\n"
          "4.Check attendace\n"
          "5.Grade assigment\n"
          "6.Exit")

def printing_menu_menager():

    print("1.List Mentors\n"
          "2.Add Mentor\n"
          "3.Remove student \n"
          "4.Exit\n")

def printing_menu_student():

    print('''
        1. Submit assignment.
        2. View my grades.
        3. Exit.
        ''')

def mentor_menu(mentor_object):

    while True:
        printing_menu_mentor()
        user_input = input("Select an option: ")
        if user_input == "1":
            table = get_from_object_to_list(mentor_object.viev_student_details())
            head = ["name", "surname", "age", "gender", "pesel", "login", "status", "date_added"]
            print_table(table, head)
        elif user_input == "2":
            name = input("Name :")
            surname = input("Surname :")
            age = input("Age :")
            gender = input("Gender :")
            password = "12345"
            pesel = input("PESEL: ")
            login = name + surname
            date_remove = ""
            status = "active"
            date_when_added = actual_date

            mentor_object.add_student(name, surname, age, gender, pesel, login, password, date_remove, status,
                                   date_when_added)
            """w każdym z tych działań trzeba dorobić zapusywanie do pliku"""
        elif user_input == "3":
            user_input2 = input("Give me Surname: ")
            for object in Student.get_all():
                if user_input2 == object.surname:
                    mentor_object.remove_mentor(object)
                    object.data_remove = actual_date
        elif user_input == "4":

            """poprawić aby wyświetlało po kolei nazwiska z listy i dalo sie to ogarnac """
            user_input2 = input("Give me Surname: ")
            attendance_status = input("1. Absent\n"
                                     "2. Late\n"
                                     "3. Present")

            for object in Student.get_all():
                if user_input2 == object.surname:
                    mentor_object.check_attendance(object, actual_date, attendance_status)
        elif user_input == "5":

            """o to to zrobie jutro rano"""
            pass
        elif user_input == "6":
            sys.exit()

def menager_menu(menager_obj):
    while True:
        printing_menu_menager()
        user_input = input("Select an option: ")
        if user_input == "1":
            table = get_from_object_to_list(menager_obj.viev_mentors())
            head = ["name", "surname", "age", "gender", "pesel", "login", "status", "date_added"]
            print_table(table, head)
        elif user_input == "2":
            name = input("Name :")
            surname = input("Surname :")
            age = input("Age :")
            gender = input("Gender :")
            password = "12345"
            pesel = input("PESEL: ")
            login = name+surname
            date_remove = ""
            status = "active"
            date_when_added = actual_date

            menager_obj.add_mentor(name, surname, age, gender, pesel, login, password, date_remove, status, date_when_added)

        elif user_input == "3":
            user_input2 = input("Give me Surname: ")
            for object in Mentor.get_all():
                if user_input2 == object.surname:
                    menager_obj.remove_mentor(object)
                    object.data_remove = actual_date
        elif user_input == "4":
            sys.exit()


def student_menu(student_obj):
    while True:
        printing_menu_student()
        user_input = input("Select an option: ")
        if user_input == '1':
            submitting_assignment(student_obj)

        elif user_input == '2':
            show_grades(student_obj)

        elif user_input == '3':
            Assignment.write_changes_to_file()
            Student.write_changes_to_file('students2.csv')
            sys.exit()

def main():
    Student.loading_file("students2.csv")  #data for instances of Student class MUST be loaded BEFORE data for instances of Assignment class
    Assignment.loading_file()

    print(Assignment.get_all())
    while True:
        printing_start_menu()
        user_input = input("Select an option:  ")


        if user_input == "1":
            object = Password_Validator("Mentor")
            if object:
                mentor_menu(object)
            else:
                print("Wrong password or disabled account")

        elif user_input == "2":
            object = Password_Validator("Menager")
            if object:
                menager_menu(object)
            else:
                print("something gona wrong")

        elif user_input == "3":
            object = Password_Validator("Student")
            if object:
                student_menu(object)
            else:
                print("Wrong password or disabled account")
        elif user_input == "4":
            if Password_Validator("Employee"):
                pass
        elif user_input == "5":
            sys.exit()
        else:
            print("no such an option")


if __name__ == "__main__":
    main()


