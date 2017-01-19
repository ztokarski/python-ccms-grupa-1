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

    def __init__(self,name, surname, age, gender, pesel, login, password, date_removed=None, status= 'Active', submissions= [],date_when_added = ''):
        '''Method that initialize instance of Student class.'''

        User.__init__(self,name, surname, age, gender, pesel, login, password, date_removed, status, date_when_added)

        self.attendances = Attendance()
        self.submissions = submissions
        self.ALL_STUDENTS.append(self)
        self.grades = []

    def submit_submission(self, link, description, assignment, grades):
        '''Method that creates instance of Submission class and adds this instance to list of all instance of
        Submission class created by the given instance of Student class.'''

        self.submissions = Submission(link,description, assignment,grades)
        self.submissions.add_submission_to_submissions_list()

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
            for index in range(len(self.submissions.submissions_list)):
                if index == len(self.submissions.submissions_list) - 1:
                    string_submissions += self.submissions.submissions_list[index].link + ',' + self.submissions.submissions_list[index].description

                else:
                    string_submissions += self.submissions.submissions_list[index].link + ',' + self.submissions.submissions_list[index].description + ','

            for element in self.submissions.submissions_list:
                for index in range(len(element.grades)):
                    if index == len(element.grades)-1:
                        string_grades += str(element.grades[index])

                    else:
                        string_grades += str(element.grades[index]) + ':'

                # if index == len(self.ASSIGNMENT_SUBMISSION[self].grades) - 1:
                #             string_submission_grades += self.ASSIGNMENT_SUBMISSION[self].grades[index]
                #
                #         else:
                #             string_submission_grades += self.ASSIGNMENT_SUBMISSION[self].grades[index]

            string_assignment_data = ''

            for element in range(len(self.submissions.submissions_list)):

                if element == len(self.submissions.submissions_list)-1:
                    string_assignment_data += self.submissions.submissions_list[element].assignment.name_assignment + ',' + self.submissions.submissions_list[element].assignment.deadline + ',' + self.submissions.submissions_list[element].assignment.date_added + ',' + self.submissions.submissions_list[element].assignment.task

                else:
                    string_assignment_data += self.submissions.submissions_list[element].assignment.name_assignment + ',' + self.submissions.submissions_list[element].assignment.deadline + ',' + self.submissions.submissions_list[element].assignment.date_added + ',' + self.submissions.submissions_list[element].assignment.task + ','

            submission_data = string_submissions + ',' + string_grades + ',' + string_assignment_data

        return [self.name, self.surname, str(self.age), self.gender, self.pesel, self.login, self._password, str(self.date_removed), self.status, str(self.date_when_added), str(attendance_dates_status), str(submission_data)]


    @classmethod
    def loading_file(cls,filename):
        '''Method that loads data from file and creats objects of student class and associated with this class objects of
        attendance and submission classes.'''

        with open(filename, 'r') as class_file:

            for line in class_file:

                line_splitted = line.strip('\n').split(',')

                one_from_students = Student(line_splitted[0], line_splitted[1], int(line_splitted[2]),
                                            line_splitted[3],
                                            line_splitted[4], line_splitted[5], line_splitted[6], line_splitted[7],
                                            line_splitted[8])

                try:   # to check whether there is submission data
                    grades = line_splitted[13].split(':')  #loading submissions grade data
                    assignment_submitted = Assignment(line_splitted[14],line_splitted[15],  line_splitted[16], line_splitted[17])  #loading data relevant for instance of Assignment class to which submission was made and creation of assignment class
                    one_from_students.submit_submission(line_splitted[11],line_splitted[12], assignment_submitted, grades)  # creating instance of Submission class


                except IndexError:
                     pass   # if there are no submission data then instance of student object is created without instances of submission class

                try:  # to check whether there is attendance data
                    attendance_dates_status = line_splitted[10].split('|')

                    separated_dates_status = []
                    for item in attendance_dates_status:
                        separated_dates_status.append(item.split(':'))


                    for element in range(len(separated_dates_status)):

                        one_from_students.attendances.checking_presence(separated_dates_status[element][0], int(separated_dates_status[element][1]))  # creating instances of Attendance class

                except IndexError:
                    pass   # if there are no attendance data then instance of student object is created without instances of attendance class

            class_file.close()

    @classmethod
    def write_changes_to_file(cls, filename):
        '''Saves data extracted from instances of Student class (by to_list method) into given file.'''

        with open(filename, "w") as class_file:
            for obj in cls.ALL_STUDENTS:

                row = ",".join(obj.to_list())

                class_file.write(row + "\n")
            class_file.close()

    @classmethod
    def get_all(cls):
        'Return all instances of Student class.'

        return cls.ALL_STUDENTS



# Student.loading_file('students.csv')
#
# #
# #
# #
# #
# Mike = Student('Mike', 'Beckingham', 22, 'Male','12345678912', 'DaveBeckingham','abc123')
# #
# # Mike.attendances.checking_presence('2088/1/20',1)
# Inventory = Assignment('Inventory','2017/2/10','2016/10/12', 'create inventory')
# To_do_list = Assignment('To_do_list','2017/1/20', '2017/1/1','create to do list')
# Mike.submit_submission('www.asbc.com','Done',To_do_list,[2,3])
#
#
# print(Assignment.get_all())
#
# #Adam = Student('Adam','Mak',22, 'Male', '12345678901','AdamM','Capac', None, 'Active','', '7/1/2016')
# #
#
# # for student in Student.get_all():
# #     student.attendances.checking_presence('2017/1/18',2)
#
# # #
# # #
# # Adam.submit_submission('www.adc.com','Assignment done', To_do_list, [5,3])
# # #
# # #
# # # #
# # # #
# # # # print(Adam.grades)
# # #
#
# # print(len(Student.get_all()))
# # for student in Student.get_all():
# #        print(student)
# #        print(student.attendances.attendance_list[0])
# #
# # # print(To_do_list.ASSIGNMENT_SUBMISSION)
# # Student.write_changes_to_file('students2.csv')
# # #
# # Assignment.write_changes_to_file('Assignment.csv')
# # #
# # Assignment.loading_file('Assignment.csv')
# # #
# # #
# # print(Assignment.get_all())
# #
# # for element in Assignment.get_all():
# #     print(element)
#
# #
# # for assignment in Assignment.get_all():
# #     print(assignment)
#
#
# #Assignment.write_changes_to_file('Assignment2.csv')