class User:
    ALL_USERS = []

    def __init__(self,name, surname, age, gender, pesel, login, password, date_added, date_removed=None, status = 'Active'):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.pesel = pesel
        self.login = login
        self.password = password
        self.date_added = date_added
        self.date_removed = date_removed
        self.status = status
        self.ALL_USERS.append(self)

    @classmethod
    def get_all(cls):
        return cls.ALL_USERS




Adam = User('Adam', 'Mickiewicz', 100, 'Male', 192345567, 'Adam','Mickiewicz','02.02.2015')


print(User.ALL_USERS)

print(User.get_all())
