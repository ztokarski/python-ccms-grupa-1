import time

from user import User


class Student(User):

    ALL_STUDENTS = []

    def __init__(self,name, surname, age, gender, pesel, login, password, date_removed=None, status= 'Active'):
        User.__init__(self,name, surname, age, gender, pesel, login, password, date_removed, status)
        self.class_attendance = Attendance.create_attendance()
        self.list_of_attendance = self.class_attendance.attendance_list
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
        return [self.name, self.surname, self.age, self.gender, self.pesel, self.login, self._password, self.date_removed, self.status, self.grades, self.list_of_attendance, self.date_added]


    @classmethod
    def loading_file(cls,filename):

        with open(filename, 'r') as class_file:

            for line in class_file:

                line_splitted = line.strip('\n').split(',')

                Student(line_splitted[0],line_splitted[1],int(line_splitted[2]), line_splitted[3],line_splitted[4],line_splitted[5],line_splitted[6],line_splitted[7],line_splitted[8])

            class_file.close()

    @classmethod
    def write_changes_to_file(cls, filename="students.csv"):
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

    def __init__(self, status = None):
        date_attendance = time.localtime()
        self.date =  '{}/{}/{}'.format(date_attendance[0], date_attendance[1], date_attendance[2])
        self.status = status
        self.attendance_list = []

    def checking_presence(self, status):
        '''Changing status of student presence at the day when attendance is checked.'''

        self.attendance_list.append(Attendance(status))

    def update_presence(self,status, date):
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

        return Attendance(0)


Student.loading_file('students.csv')

for student in Student.get_all():
    student.class_attendance.checking_presence(2)

for student in Student.get_all():
    for attendance in student.list_of_attendance:
        print(attendance)

Student.write_changes_to_file('students.csv')


