import time

class User:
    '''Class containing basic data pertaining to all users of the system.'''

    ALL_USERS = []  #to store all instances of User class

    def __init__(self, name, surname, age, gender, pesel, login, password, date_removed=None, status = 'Active'):
        '''Initialize User object. '''

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
    def loading_file(self,filename):

        with open(filename, 'r') as class_file:
            count = 1
            for line in class_file:
                print(line)
                User(line[0],line[1],line[2], line[3],line[4],line[5],line[6],line[7],line[8])



    @classmethod
    def get_all(cls):
        'Return all instances of User class.'

        return cls.ALL_USERS


