
class Assignment:
    '''Assignment class containing data pertaining to assignment created by Mentor.'''

    ASSIGNMENTS = []

    def __init__(self, name_assignment, deadline, date_added,task):
        self.name_assignment = name_assignment
        self.deadline = deadline
        self.date_added = date_added
        self.task = task
        self.ASSIGNMENTS.append(self)

    def __str__(self):

        return 'Assignment: {}; Task: {}; Deadline: {}; Added by Mentor: {}.'.format(self.name_assignment, self.task, self.deadline, self.date_added)

    def to_list(self):
        '''Method that extracts data from Assigment class and converts it into string.'''


        string_assignment_data = ''

        string_assignment_data += self.name_assignment + ',' + self.deadline + ',' + self.date_added + ',' + self.task

        return [string_assignment_data]

    @classmethod
    def write_changes_to_file(cls, filename='data/Assignment.csv'):
        '''Saves data extracted from instances of Student class (by to_list method) into given file.'''

        with open(filename, "w") as class_file:
            for assignment in cls.ASSIGNMENTS:

                row = ",".join(assignment.to_list())

                class_file.write(row + "\n")
            class_file.close()

    @classmethod
    def loading_file(cls, filename='data/Assignment.csv'):
        '''Method that loads data from file and creats objects of assigment class'''

        with open(filename, 'r') as class_file:

            Assignment.ASSIGNMENTS = []
            for line in class_file:

                line_splitted = line.strip('\n').split(',')
                Assignment(line_splitted[0], line_splitted[1], line_splitted[2], line_splitted[3])

            class_file.close()

    @classmethod
    def get_all(cls):
        return cls.ASSIGNMENTS













