import time

class User:
    '''Class containing basic data pertaining to all users of the system.'''

    ALL_USERS = []  #to store all instances of User class

    def __init__(self, name, surname, age, gender, pesel, login, password, date_removed=None, status = 'Active',date_when_added =''):
        '''Method that initializes User object. '''

        #if not(pesel.isdigit()) or len(pesel) != 11:
         #   raise ValueError('Pesel has to contain 11 numbers.')

        #if gender not in ('Male', 'Female'):
        #    raise ValueError('Gender has to be either Male or Female')

        #if type(age) != int:
        #   raise ValueError('Age has to be integer.')

        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.pesel = pesel
        self.login = login
        self._password = password
        self.date_removed = date_removed
        self.status = status
        self.ALL_USERS.append(self)
        self.date_when_added = date_when_added

    def validate_password(self, given_password):
        '''Method that validates password and provide access to the user account.'''

        if given_password == self._password:
            return True

        else:
            return False


    @classmethod
    def get_all(cls):
        'Class method that returns all instances of User class.'

        return cls.ALL_USERS



