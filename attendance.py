
class Attendance():
    '''Attendance class containing data pertaining to all student attendance as well as each student attendance.'''

    def __init__(self, date = ' ', status = '0'):
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

        if self.status == '2':
            student_status = 'present'

        elif self.status == '1':
            student_status = 'late'

        elif self.status == '0':
            student_status = 'absent'

        else:
            student_status = '....'

        return 'Student was {} at the day {}.'.format(student_status, self.date)
