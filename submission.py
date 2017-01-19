"""Submission"""

from assigment import Assignment


class Submission():
    '''Class that contain data pertaining to Student submissions to assignments (link,description of each submission,
    assignment to which submission each is made, grades given for eachsubmission and list of all submissions
    made by the student).  '''

    def __init__(self,link,description, assignment,grades):
        '''Method that initialize instance of Submission class.'''

        self.link = link
        self.description = description
        self.grades = grades
        self.assignment = assignment

    def __str__(self):
        '''Method that overwrittes default __str__ method and returns string with basic data taken from instance
        of submission class.'''

        return 'Submission to {} assignment. Link: {}, Description: {}, Grades given: {}'.format(self.assignment.name_assignment,self.link, self.description, self.grades)

