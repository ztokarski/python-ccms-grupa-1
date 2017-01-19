import time

from user import User
from assigment import Assignment
from submission import Submission
from attendance import Attendance


class Student(User):
    '''Class inheriting from User, containing student personal data as well as information about submissions to assignment
    (grades given for each submission, other information pertaining to submission) and Student attendance).
    '''

    ALL_STUDENTS = []  # list containing all instances of Student class

    def __init__(self,name, surname, age, gender, pesel, login, password, date_removed=None, status= 'Active',date_when_added = 'None'):
        '''Method that initialize instance of Student class.'''

        User.__init__(self,name, surname, age, gender, pesel, login, password, date_removed, status, date_when_added)

        self.attendances = Attendance()

        self.ALL_STUDENTS.append(self)
        self.grades = []
        self.state = False
        self.submissions = []


    def submit_submission(self, link, description, assignment, grades):
        '''Method that creates instance of Submission class and adds this instance to list of all instance of
        Submission class created by the given instance of Student class.'''

        self.submissions.append(Submission(link, description, assignment, grades))


    def get_grades(self):
        if self.submissions:
            for submission in self.submissions.submissions_list:
                self.grades.extend(submission.grades)

    def give_instance_values(self):
        return (self.name, self.surname, self.age, self.gender, self.pesel, self.login, self.password, self.date_removed, self.status, self.date_when_added)

    def __str__(self):
        '''Method that overwrittes default __str__ method and returns string with basic student data.'''

        self.get_grades()

        string_grades = ''

        for index in range(len(self.grades)):
            if index == len(self.grades) -1:
                string_grades += str(self.grades[index])

            else:
                string_grades += str(self.grades[index]) + ','

        return 'Student: {} {}, age: {}, gender: {}, PESEL: {}, Status: {}, Grades: {}.'.format(self.name, self.surname, self.age, self.gender, self.pesel, self.status, string_grades)

    def to_list(self):
        '''Method that extracts data from student class and converts it into string.'''

        attendance_dates_status = ''

        for attendance in self.attendances.attendance_list:
            attendance_dates_status += attendance.date + ':' + str(attendance.status) + '|'

        string_submissions = ''

        string_grades = ''

        submission_data = ''
        if self.submissions:
            for index in range(len(self.submissions)):
                if index == len(self.submissions) - 1:
                    string_submissions += self.submissions[index].link + ':' + self.submissions[index].description

                else:
                    string_submissions += self.submissions[index].link + ':' + self.submissions[index].description + '|'

            for element in self.submissions:
                for index in range(len(element.grades)):
                    if index == len(element.grades)-1:
                        string_grades += str(element.grades[index])

                    else:
                        string_grades += str(element.grades[index]) + ':'


            string_assignment_data = ''

            for element in range(len(self.submissions)):

                if element == len(self.submissions)-1:
                    string_assignment_data += self.submissions[element].assignment.name_assignment + ':' + self.submissions[element].assignment.deadline + ':' + self.submissions[element].assignment.date_added + ':' + self.submissions[element].assignment.task

                else:
                    string_assignment_data += self.submissions[element].assignment.name_assignment + ':' + self.submissions[element].assignment.deadline + ':' + self.submissions[element].assignment.date_added + ':' + self.submissions[element].assignment.task + '|'

            submission_data = string_submissions + ',' + string_grades + ',' + string_assignment_data
            print(submission_data)

        return [self.name, self.surname, str(self.age), self.gender, self.pesel, self.login, self._password, str(self.date_removed), self.status, str(self.date_when_added), str(attendance_dates_status), str(submission_data)]


    @classmethod
    def loading_file(cls,filename = 'students.csv'):
        '''Method that loads data from file and creats objects of student class and associated with this class objects of
        attendance and submission classes.'''

        with open(filename, 'r') as class_file:

            for line in class_file:

                line_splitted = line.strip('\n').split(',')

                one_from_students = Student(str(line_splitted[0]), str(line_splitted[1]), str(line_splitted[2]),
                                            str(line_splitted[3]),
                                            str(line_splitted[4]), str(line_splitted[5]), str(line_splitted[6]), str(line_splitted[7]),
                                            str(line_splitted[8]),str(line_splitted[9]))

                try:
                    grades = line_splitted[12].split(':')  # to check whether there are grades

                except:
                    grades = []  # inserting default empty list

                try:   # to check whether there is submission data

                    assignment_data = line_splitted[13].split('|')

                    separated_assignment_data = []

                    for item in assignment_data:
                        separated_assignment_data.append(item.split(':'))

                    sole_submission_data = line_splitted[11].split('|')
                    separated_sole_submission_data = []

                    for item in sole_submission_data:
                        separated_sole_submission_data.append(item.split(':'))

                    for element in range(len(separated_assignment_data)):

                        assignment_submitted = Assignment(separated_assignment_data[element][0], separated_assignment_data[element][1], separated_assignment_data[element][2], separated_assignment_data[element][3])   #loading data relevant for instance of Assignment class to which submission was made and creation of assignment clas

                        one_from_students.submit_submission(separated_sole_submission_data[element][0], separated_sole_submission_data[element][1], assignment_submitted, grades)  # creating instance of Submission class


                except IndexError:
                     pass   # if there are no submission data then instance of student object is created without instances of submission class

                try:  # to check whether there is attendance data
                    attendance_dates_status = line_splitted[10].split('|')

                    separated_dates_status = []
                    for item in attendance_dates_status:
                        separated_dates_status.append(item.split(':'))


                    for element in range(len(separated_dates_status)):

                        one_from_students.attendances.checking_presence(separated_dates_status[element][0], separated_dates_status[element][1])  # creating instances of Attendance class

                except IndexError:
                    pass   # if there are no attendance data then instance of student object is created without instances of attendance class

            class_file.close()

    @classmethod
    def write_changes_to_file(cls, filename='students.csv'):
        '''Saves data extracted from instances of Student class (by to_list method) into given file.'''

        with open(filename, "w") as class_file:
            for student in cls.ALL_STUDENTS:

                row = ",".join(student.to_list())

                class_file.write(row + "\n")
            class_file.close()

    @classmethod
    def get_all(cls):
        'Return all instances of Student class.'

        return cls.ALL_STUDENTS



#Student.loading_file('students2.csv')
# # # # persons.age, persons.gender, persons.pesel, persons.login, persons.status, persons.date_when_adde
# # #
# # for student in Student.get_all():
# #      print(type(student.name))
# #      print(type(student.surname))
# #      print(type(student.age))
# #      print(type(student.pesel))
# #      print(type(student.login))
# #      print(type(student.status))
# #      print(type(student.date_when_added))
# #
# # Student.write_changes_to_file('students2.csv')
# #
# #
# # #
# # Student.loading_file('students2.csv')
# # #
# # for student in Student.get_all():
# #     print(type(student.name))
# #     print(type(student.surname))
# #     print(type(student.age))
# #     print(type(student.pesel))
# #     print(type(student.login))
# #     print(type(student.status))
# #     print(type(student.date_when_added))
# #
# # a = None
# # for student in Student.get_all():
# #      if student.surname == 'Milecka':
# #          a = student
# # #
# # #
# # print(a)
# # #
# # a.attendances.checking_presence('2017/1/10','1')
# # a.attendances.update_presence('2017/1/10','2')
# # for attendance in a.attendances.attendance_list:
# #      print(a)
# #      print(attendance)
# # #
# #
# #
# # #
# # # #
# # # #
# # # #
# # # #
# Mike = Student('Mike', 'Beckingham', '22', 'Male','12345678912', 'DaveBeckingham','abc123')
# # # # #
# ## Mike.attendances.checking_presence('2088/1/20','1')
# Inventory = Assignment('Inventory','2017/2/10','2016/10/12', 'create inventory')
# To_do_list = Assignment('To_do_list','2017/1/20', '2017/1/1','create to do list')
# Mike.submit_submission('www.asbc.com','Done',To_do_list,[])
# # #for submission in Mike.submissions:
# #  #   print(submission)
# #
# Mike.submit_submission('www.gd.com', 'hard',Inventory, [])
# #
# # # for submission in Mike.submissions:
# # #     print(submission)
# # #
# # for student in Student.get_all():
# #     print(student.submissions)
# Student.write_changes_to_file('students2.csv')
#
#
# #
# # print(Assignment.get_all())
# #
# # #Adam = Student('Adam','Mak',22, 'Male', '12345678901','AdamM','Capac', None, 'Active','', '7/1/2016')
# # #
# #
# for student in Student.get_all():
#      student.attendances.checking_presence('2017/1/18','2')
# #
# # # #
# # # #
# # # Adam.submit_submission('www.adc.com','Assignment done', To_do_list, [5,3])
# # # #
# # # #
# # # # #
# # # # #
# # # # # print(Adam.grades)
# # # #
# #
# # # print(len(Student.get_all()))
# for student in Student.get_all():
#        print(student)
#        print(student.attendances.attendance_list[0])
# # #
# Student.write_changes_to_file('students2.csv')
#
# for student in Student.get_all():
#        print(student)
#        print(student.attendances.attendance_list[0])
#
# # # print(len(Student.get_all()))
# # for student in Student.get_all():
# #        print(student)
# #        print(student.attendances.attendance_list[0])
# #
# # # print(To_do_list.ASSIGNMENT_SUBMISSION)
# # Student.write_changes_to_file('students2.csv')
# #
# # Assignment.write_changes_to_file('Assignment.csv')
# #
# # Assignment.loading_file('Assignment.csv')
# #
# #
# # print(Assignment.get_all())
# #
# # for assignment in Assignment.get_all():
# #     print(assignment)
# #
# #
# # Assignment.write_changes_to_file('Assignment2.csv')
#
# # # # print(To_do_list.ASSIGNMENT_SUBMISSION)
# # # Student.write_changes_to_file('students2.csv')
# # # #
# # # Assignment.write_changes_to_file('Assignment.csv')
# # # #
# # # Assignment.loading_file('Assignment.csv')
# # # #
# # # #
# # # print(Assignment.get_all())
# # #
# # # for element in Assignment.get_all():
# # #     print(element)
# #
# # #
# # # for assignment in Assignment.get_all():
# # #     print(assignment)
# #
# #
# # #Assignment.write_changes_to_file('Assignment2.csv')
