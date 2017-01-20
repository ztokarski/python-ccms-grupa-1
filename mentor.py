from employee import Employee
from student import Student

class Mentor(Employee):

    MENTOR_LIST = []

    def __init__(self,name, surname, age, gender, pesel, login, password, date_removed, status, date_when_added):
        Employee.__init__(self, name, surname, age, gender, pesel, login, password, date_removed, status, date_when_added)

    def add_student(self, name, surname, age, gender, pesel, login, password, date_removed, status, date_when_added):
        Student().ALL_STUDENTS.append(Student(name, surname, age, gender, pesel, login, password, date_removed, status, date_when_added))

    def make_assigment():
        pass

    def grade_subbmission():
        pass

    def check_attendance():
        pass

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