import sys
from student import *
from user import *
from assigment import *
from attendance import *
from mentor import *
from menager import *

def Password_Validator(type):           #returns object
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
            if element.login == login:
                if element._password == password:
                    return element
    if type == "Student":
        for element in Student.get_all():
            if element.login == login:
                if element._password == password:
                    print('Student')
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

def main():


    while True:
        printing_start_menu()
        user_input = input("Select an option:  ")


        if user_input == "1":
            Password_Validator("Mentor")
        elif user_input == "2":
            Password_Validator("Menager")
        elif user_input == "3":
            Password_Validator("Student")
        elif user_input == "4":
            Password_Validator("Employee")
        elif user_input == "5":
            sys.exit()
        else:
            print("not such an option")

if __name__ == "__main__":
    main()

# def main():
#
#
#     while True:
#         option = input("Select an option:\n"
#                        "1.Mentor\n"
#                        "2.Menager\n"
#                        "3.Student\n"
#                        "4.Employee\n"
#                        "5.Exit\n")
#
#         if option == "1":
#             Password_Validator("Mentor")
#
#         elif option == "2":
#             Password_Validator("Menager")
#
#         elif option == "3":
#             Password_Validator("Student")
#
#         elif option == "4":
#             Password_Validator("Employee")
#
#         elif option == "5":
#             sys.exit()

if __name__ == "__main__":
    main()

