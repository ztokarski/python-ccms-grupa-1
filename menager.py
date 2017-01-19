from employee import Employee
from mentor import Mentor


class Menager(Employee):

    MENAGER_LIST = []

    def __init__(self,name, surname, age, gender, pesel, login, password, date_remove, status, date_when_added):
        Employee.__init__(self, name, surname, age, gender, pesel, login, password, date_remove, status, date_when_added)
    #
    # def viev_student_details(): //// funkcja dziedziczona z klasy Employee
    #     pass

    def add_mentor(self,name, surname, age, gender, pesel, login, password, date_remove, status, date_when_added):
        Mentor.MENTOR_LIST.append(Mentor(name, surname, age, gender, pesel, login, password, date_remove, status, date_when_added))

    def remove_mentor(self,mentor_obj):  ## wchodzimy objektem w którym chcemy to zmienic
        mentor_obj.status = "disable"

    def viev_mentors():  ## zwraca nam po prostu liste obiektów clasy mentor
        Mentor.get_all()

    def to_list(self):
        return [self.name, self.surname, self.age, self.gender, self.pesel, self.login, self._password, self.date_removed, self.status, self.date_when_added]

    @classmethod
    def loading_file(cls,filename = "menagers.csv"):
        cls.MENAGER_LIST = []
        with open(filename, 'r') as class_file:
            count = 1
            for line in class_file:
                line = line.replace("\n", "").split(",")
                cls.MENAGER_LIST.append(Menager(line[0],line[1],line[2], line[3],line[4],line[5],line[6],line[7],line[8], line[9]))

    @classmethod
    def write_changes_to_file(cls,filename = "menagers.csv"):
        with open(filename, "w") as class_file:
            for obj in cls.MENAGER_LIST:
                row = ",".join(obj.to_list())
                class_file.write(row + "\n")

    @classmethod
    def get_all(cls):
        return cls.MENAGER_LIST



# Menager.loading_file()
# Mentor.loading_file()
#
# Menager.MENAGER_LIST[0].add_mentor("Andrzej", "duda", "24", "M", "12345", "AD", "policja", "None", "active", "2018")
# Mentor.write_changes_to_file()
#
# for item in Mentor.get_all():
#
#     print("cok")
#     print(item.__dict__)