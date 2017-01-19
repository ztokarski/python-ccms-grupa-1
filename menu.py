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

        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
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


def main():


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
            if Password_Validator("Student"):
                pass
        elif user_input == "4":
            if Password_Validator("Employee"):
                pass
        elif user_input == "5":
            sys.exit()
        else:
            print("not such an option")

if __name__ == "__main__":
    main()


