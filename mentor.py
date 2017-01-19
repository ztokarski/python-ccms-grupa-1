from employee import Employee
from student import Student
from submission import Submission
from assigment import  Assignment

class Mentor(Employee):

    MENTOR_LIST = []

    def __init__(self,name, surname, age, gender, pesel, login, password, date_removed, status, date_when_added):
        Employee.__init__(self, name, surname, age, gender, pesel, login, password, date_removed, status, date_when_added)

    def add_student(self, name, surname, age, gender, pesel, login, password, date_removed, status, date_when_added):
        Student.ALL_STUDENTS.append(Student(name, surname, age, gender, pesel, login, password, date_removed, status, date_when_added))

    def make_assigment(self, name_assignment, deadline, date_added,task):
        Assignment(name_assignment, deadline, date_added,task)

    def grade_subbmission(self, student_obj, grade): ## jako arg podajemy obiekt klasy student i ta funkcja zmienia temu obiektowi ocene w ostatnim nieocenionym submission
        if  not student_obj.submissions.submission_list[-1].grades:
             student_obj.submissions.submission_list[-1].grades.append(grade)  ##grade to lista z ocenami np [2,3,5]
        else:
            print("pusta lista")
            # raise LookupError "Already graded"

    def check_attendance(self, student_obj, date, status):
            student_obj.attendences.check_presence(date, status)

    def to_list(self):
        return [self.name, self.surname, self.age, self.gender, self.pesel, self.login, self._password, self.date_removed, self.status, self.date_when_added]

    @classmethod
    def loading_file(cls, filename="mentors.csv"):
        cls.MENTOR_LIST = []
        with open(filename, 'r') as class_file:
            count = 1
            for line in class_file:
                line = line.replace("\n", "").split(",")
                cls.MENTOR_LIST.append(
                    Mentor(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9]))


    @classmethod
    def write_changes_to_file(cls,filename = "mentors.csv"):
        with open(filename, "w") as class_file:
            for obj in cls.MENTOR_LIST:
                row = ",".join(obj.to_list())
                class_file.write(row + "\n")


    @classmethod
    def get_all(cls):
        return cls.MENTOR_LIST

# Mentor.loading_file()
# print(Mentor.get_all())
# for item in Employee.get_all():
#     print("cok")
#     print(item.__dict__)