import time

from user import User
from assigment import Assignment
from submission import Submission


class Student(User):
    '''Class inheriting from User, containing student personal data as well as information about submissions to assignment
    (grades given for each submission, other information pertaining to submission) and Student attendance).
    '''

    ALL_STUDENTS = []  #list containing all instances of Student class

    def __init__(self,name, surname, age, gender, pesel, login, password, date_removed=None, status= 'Active',submissions= [],date_when_added = ''):
        '''Method that initialize instance of Student class.'''

        User.__init__(self,name, surname, age, gender, pesel, login, password, date_removed, status, date_when_added)

        self.list_of_attendance = Attendance()
        self.submissions = submissions
        self.ALL_STUDENTS.append(self)

    def submit_submission(self, link, description,assignment):
        '''Method that creates instance of Submission class and adds this instance to list of all instance of
        Submission class created by the given instance of Student class.'''

        self.submissions = Submission(link,description,assignment)

        self.submissions.add_submission_to_submissions_list()

    def __str__(self):
        '''Method that overwrittes default __str__ method and returns string with basic student data.'''

        grades = ''
        if self.submissions:  #extracting grades from all submission object
            for submission in self.submissions.submissions_list:
                for grade in range(len(submission.grades)):
                    if grade == len(submission.grades)-1:

                        grades += str(submission.grades[grade])

                    else:
                        grades += str(submission.grades[grade]) + ','

        return 'Student: {} {}, age: {}, gender: {}, PESEL: {}, Status: {}, Grades: {}.'.format(self.name, self.surname, self.age, self.gender, self.pesel, self.status, grades)

    def to_list(self):
        '''Method that extracts data from student class and converts it into string.'''

        attendance_dates_status = ''

        for attendance in self.list_of_attendance.attendance_list:
            attendance_dates_status += attendance.date + ':' + str(attendance.status) + '|'

        submissions = []

        if self.submissions:
            for submission in self.submissions.submissions_list:
                submission_data = [submission.link, submission.description, str(submission.grades)]
                submissions.append(submission_data)

        return [self.name, self.surname, str(self.age), self.gender, self.pesel, self.login, self._password, str(self.date_removed), self.status, str(self.date_when_added), str(attendance_dates_status), str(submissions)]


    @classmethod
    def loading_file(cls,filename):
        '''Method that loads data from file and creats objects of student class and associated with this class objects of
        attendance and submission classes.'''

        with open(filename, 'r') as class_file:

            for line in class_file:

                line_splitted = line.strip('\n').split(',')

                try:   # to check whether there is submission data
                    one_from_students = Student(line_splitted[0], line_splitted[1], int(line_splitted[2]),
                                                line_splitted[3],
                                                line_splitted[4], line_splitted[5], line_splitted[6], line_splitted[7],
                                                line_splitted[8])

                    one_from_students.submit_submission(line_splitted[11],line_splitted[12], line_splitted[13])  # creating instance of Submission class


                except IndexError:
                    one_from_students = Student(line_splitted[0], line_splitted[1], int(line_splitted[2]),
                                                line_splitted[3],
                                                line_splitted[4], line_splitted[5], line_splitted[6], line_splitted[7],
                                                line_splitted[8])

                try:  # to check whether there is attendance data
                    attendance_dates_status = line_splitted[10].split('|')

                    separated_dates_status = []
                    for item in attendance_dates_status:
                        separated_dates_status.append(item.split(':'))


                    for element in range(len(separated_dates_status)):

                        one_from_students.list_of_attendance.checking_presence(separated_dates_status[element][0], int(separated_dates_status[element][1]))  # creating instances of Attendance class

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


class Attendance():
    '''Attendance class containing data pertaining to all student attendance as well as each student attendance.'''

    def __init__(self, date = ' ', status = 0):
        '''Method that initialize instance of Attendance class.'''

        self.date =  date
        self.status = status
        self.attendance_list = []

    def checking_presence(self, date, status):
        '''Changing status of student presence at the day when attendance is checked.'''

        self.attendance_list.append(Attendance(date, status))

    def update_presence(self,date, status):
        '''Changing status of student presence at selected day.'''

        for day_at_school in self.attendance_list:
            if day_at_school.date == date:
                day_at_school.status = status
                return

        raise ValueError('There is no such date.')

    def __str__(self):
        '''Method that overwrittes default __str__ method and changes student status from int into string and
        returns string with basic data from instance of attendance class.'''

        if self.status == 2:
            student_status = 'present'

        elif self.status == 1:
            student_status = 'late'

        elif self.status == 0:
            student_status = 'absent'

        return 'Student was {} at the day {}.'.format(student_status, self.date)



# class Submission():
#     '''Class that contain data pertaining to Student submissions to assignments (link,description of each submission,
#     assignment to which submission each is made, grades given for eachsubmission and list of all submissions
#     made by the student).  '''
#
#     def __init__(self,link,description, assignment,grades=[3,2]):
#         '''Method that initialize instance of Submission class.'''
#
#         self.link = link
#         self.description = description
#         self.grades = grades
#         self.assignment = assignment
#         self.submissions_list = []
#
#
#     def add_submission_to_submissions_list(self):
#         '''Method that creates submission object and appends it to list of all submission object by the given
#         instance of student class.'''
#
#         self.submissions_list.append(Submission(self.link,self.description,self.assignment,self.grades))
#
#     def __str__(self):
#         '''Method that overwrittes default __str__ method and returns string with basic data taken from instance
#         of submission class.'''
#
#         return 'Submission to {} assignment. Link: {}, Description: {}, Grades given: {}'.format(self.assignment,self.link, self.description, self.grades)

