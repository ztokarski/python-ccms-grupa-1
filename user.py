import time


class User:
    '''Class containing basic data pertaining to all users of the system.'''

    ALL_USERS = []  #to store all instances of User class

    def __init__(self,name, surname, age, gender, pesel, login, password, date_removed=None, status = 'Active'):
        '''Initialize User object. '''

        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.pesel = pesel
        self.login = login
        self._password = password
        date_when_added = time.localtime()
        self.date_added = '{}/{}/{}'.format(date_when_added[0], date_when_added[1], date_when_added[2])
        self.date_removed = date_removed
        self.status = status
        self.ALL_USERS.append(self)


    def validate_password(self, given_password):
        '''To validate password and provide access to the user account.'''

        if given_password == self._password:
            return True

        else:
            return False


    @classmethod
    def get_all(cls):
        'Return all instances of User class.'

        return cls.ALL_USERS




Adam = User('Adam', 'Mickiewicz', 100, 'Male', 192345567, 'Adam','Mickiewicz')

print(Adam.date_added)
print(User.ALL_USERS)

print(User.get_all())

print(Adam.validate_password('abc'))

print(Adam.validate_password('Mickiewicz'))



