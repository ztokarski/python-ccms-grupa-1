import time

from user import User


class Student(User):

    ALL_STUDENTS = []

    def __init__(self,name, surname, age, gender, pesel, login, password, date_removed=None, status= 'Active',submissions= []):
        User.__init__(self,name, surname, age, gender, pesel, login, password, date_removed, status)
        self.class_attendance = Attendance.create_attendance()
        self.list_of_attendance = self.class_attendance
        self.submissions = submissions
        self.ALL_STUDENTS.append(self)

    def submit_submission(self, link, description,assignment):

        self.submissions = Submission(link,description,assignment)

        self.submissions.add_submission_to_submissions_list()

    def view_submissions(self):

        return self.submissions

    def __str__(self):

        grades = ''
        if self.submissions:
            for submission in self.submissions.submissions_list:
                for grade in range(len(submission.grades)):
                    if grade == len(submission.grades)-1:

                        grades += str(submission.grades[grade])

                    else:
                        grades += str(submission.grades[grade]) + ','

        return 'Student: {} {}, age: {}, gender: {}, PESEL: {}, Status: {}, Grades: {}.'.format(self.name, self.surname, self.age, self.gender, self.pesel, self.status, grades)

    def to_list(self):

        attendance_dates_status = ''

        for attendance in self.list_of_attendance.attendance_list:
            attendance_dates_status += attendance.date + ':' + str(attendance.status) + '|'


        submissions = []


        if self.submissions:
            for submission in self.submissions.submissions_list:
                submission_data = [submission.link, submission.description, str(submission.grades)]
                submissions.append(submission_data)

        return [self.name, self.surname, str(self.age), self.gender, self.pesel, self.login, self._password, str(self.date_removed), self.status, str(self.date_added), str(attendance_dates_status), str(submissions)]


    @classmethod
    def loading_file(cls,filename):

        with open(filename, 'r') as class_file:

            for line in class_file:

                line_splitted = line.strip('\n').split(',')

                try:
                    print(line_splitted[11],line_splitted[12], line_splitted[13])


                    one_from_students = Student(line_splitted[0], line_splitted[1], int(line_splitted[2]),
                                                line_splitted[3],
                                                line_splitted[4], line_splitted[5], line_splitted[6], line_splitted[7],
                                                line_splitted[8])

                    one_from_students.submit_submission(line_splitted[11],line_splitted[12], line_splitted[13])

                except IndexError:
                    one_from_students = Student(line_splitted[0], line_splitted[1], int(line_splitted[2]),
                                                line_splitted[3],
                                                line_splitted[4], line_splitted[5], line_splitted[6], line_splitted[7],
                                                line_splitted[8])
                try:
                    attendance_dates_status = line_splitted[10].split('|')

                    separated_dates_status = []
                    for item in attendance_dates_status:
                        separated_dates_status.append(item.split(':'))


                    for element in range(len(separated_dates_status)):

                        one_from_students.list_of_attendance.checking_presence(separated_dates_status[element][0], int(separated_dates_status[element][1]))

                except IndexError:
                    pass

            class_file.close()

    @classmethod
    def write_changes_to_file(cls, filename):

        with open(filename, "w") as class_file:
            for obj in cls.ALL_STUDENTS:

                row = ",".join(obj.to_list())

                class_file.write(row + "\n")
            class_file.close()

    @classmethod
    def get_all(cls):
        'Return all instances of User class.'

        return cls.ALL_STUDENTS


class Attendance():
    '''Attendance class containing data pertaining to all student attendance as well as each student attendance.'''

    def __init__(self, date = ' ', status = 0):

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

        if self.status == 2:
            student_status = 'present'

        elif self.status == 1:
            student_status = 'late'

        elif self.status == 0:
            student_status = 'absent'

        return 'Student was {} at the day {}.'.format(student_status, self.date)

    @classmethod
    def create_attendance(cls):

        return Attendance()


class Submission():

    def __init__(self,link,description, assignment,grades=[3,2]):
        self.link = link
        self.description = description
        self.grades = grades
        self.assignment = assignment
        self.submissions_list = []


    def add_submission_to_submissions_list(self):
        self.submissions_list.append(Submission(self.link,self.description,self.assignment,self.grades))



Student.loading_file('students2.csv')



#Mike = Student('Mike', 'Beckingham', 22, 'Male','12345678912', 'DaveBeckingham','abc123')

#Mike.list_of_attendance.checking_presence('2088/1/20',1)


#Mike.submit_submission('www.asbc.com','Done','To_do_list')

for student in Student.get_all():
     print(student)



Student.write_changes_to_file('students2.csv')
