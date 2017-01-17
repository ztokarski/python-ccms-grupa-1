from employee import Employee

class Menager(Employee):

    MENAGER_LIST = []

    def __init__(self,name, surname, age, gender, pesel, login, password, date_addeed, date_remove, status):
        Employee.__init__(name, surname, age, gender, pesel, login, password, date_addeed, date_remove, status)

    def viev_student_details():
        pass

    def add_mentor():
        pass

    def remove_mentor():
        pass

    def viev_mentors():
        pass

    def to_list(self):
        return [self.name, self.surname, self.age, self.gender, self.pesel, self.login, self._password, self.date_removed, self.status, self.date_added]

    @classmethod
    def loading_file(cls,filename = "menagers.csv"):
        cls.MENAGER_LIST = []
        with open(filename, 'r') as class_file:
            count = 1
            for line in class_file:
                line = line.split(",")
                cls.MENAGER_LIST.append(Menager(line[0],line[1],line[2], line[3],line[4],line[5],line[6],line[7],line[8]))

    @classmethod
    def write_changes_to_file(cls,filename = "menagers.csv"):
        with open(filename, "w") as class_file:
            for obj in cls.MENAGER_LIST:
                row = ",".join(obj.to_list())
                class_file.write(row + "\n")

    @classmethod
    def get_all(cls):
        return cls.MENAGER_LIST

Menager.loading_file()
print(Menager.get_all())