from user import User
from student import Student

class Employee(User):
    EMPLOYEE_LIST = []

    def __init__(self, name, surname, age, gender, pesel, login, password, date_remove, status, date_when_added):
        super().__init__(name, surname, age, gender, pesel, login, password, date_remove, status, date_when_added)

    def viev_student_details(self):
        return Student.get_all()

    # def create_employee():
    #     pass

    def to_list(self):
        return [self.name, self.surname, self.age, self.gender, self.pesel, self.login, self._password, self.date_removed, self.status, self.date_when_added]

    @classmethod
    def loading_file(cls,filename = "employees.csv"):
        cls.EMPLOYEE_LIST = []
        with open(filename, 'r') as class_file:
            count = 1
            for line in class_file:
                line = line.replace("\n","").split(",")
                emp = Employee(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])
                cls.EMPLOYEE_LIST.append(emp)
            class_file.close()

    @classmethod
    def write_changes_to_file(cls,filename = "employees.csv"):
        with open(filename, "w") as class_file:
            for obj in cls.EMPLOYEE_LIST:
                row = ",".join(obj.to_list())
                class_file.write(row + "\n")


    @classmethod
    def get_all(cls):
         return cls.EMPLOYEE_LIST


#
# Employee.loading_file()
#
# Employee.write_changes_to_file()
#
# for item in Employee.get_all():
#     print("cok")
#     print(item.__dict__)
#
