import time

from user import User


class Student(User):

    ALL_STUDENTS = []

    def __init__(self,name, surname, age, gender, pesel, login, password, date_removed=None, status= 'Active'):
        User.__init__(self,name, surname, age, gender, pesel, login, password, date_removed, status)
        self.class_attendance = Attendance.create_attendance()
        self.list_of_attendance = self.class_attendance
        self.submissions = []
        self.grades = []
        self.ALL_STUDENTS.append(self)

    def create_submission(self, link, description):

        self.submissions.append(Submission(link,description))

    def view_submissions(self):

        return self.submissions

    def __str__(self):

        return 'Student: {} {}, age: {}, gender: {}, PESEL: {}, Status: {}, Grades: {}'.format(self.name, self.surname, self.age, self.gender, self.pesel, self.status, self.grades)

    def to_list(self):

        attendance_dates_status = ''

        for attendance in self.list_of_attendance.attendance_list:
            print(attendance.date)
            print(attendance.status)
            attendance_dates_status += attendance.date + ':' + str(attendance.status) + '|'

        return [self.name, self.surname, str(self.age), self.gender, self.pesel, self.login, self._password, str(self.date_removed), self.status, self.date_added, attendance_dates_status]


    @classmethod
    def loading_file(cls,filename):

        with open(filename, 'r') as class_file:

            for line in class_file:

                line_splitted = line.strip('\n').split(',')

                try:

                    attendance_dates_status = line_splitted[10].split('|')

                    separated_dates_status = []
                    for item in attendance_dates_status:
                        separated_dates_status.append(item.split(':'))

                    one_from_students = Student(line_splitted[0],line_splitted[1],int(line_splitted[2]), line_splitted[3],line_splitted[4],line_splitted[5],line_splitted[6],line_splitted[7],line_splitted[8])


                    print(separated_dates_status)
                    for element in range(len(separated_dates_status)):

                        one_from_students.list_of_attendance.checking_presence(separated_dates_status[element][0], int(separated_dates_status[element][1]))

                except IndexError:
                    Student(line_splitted[0], line_splitted[1], int(line_splitted[2]), line_splitted[3], line_splitted[4], line_splitted[5], line_splitted[6], line_splitted[7], line_splitted[8])

            class_file.close()

    @classmethod
    def write_changes_to_file(cls, filename):
        with open(filename, "w") as class_file:
            for obj in cls.ALL_STUDENTS:
                print(obj)
                row = ",".join(obj.to_list())
                print(row)
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


Student.loading_file('students.csv')

for student in Student.get_all():
    student.list_of_attendance.checking_presence('2017/1/17',2)
    student.list_of_attendance.checking_presence('2017/2/18',2)
    student.list_of_attendance.checking_presence('2018/3/19', 1)

Dave = Student('Dave', 'Beckingham', 22, 'Male','12345678912', 'DaveBeckingham','abc123')

Dave.list_of_attendance.checking_presence('2017/1/17',2)


Student.write_changes_to_file('students2.csv')
