"""Submission"""
"""ATR link, disc, grades"""



class Submission():
    '''Class that contain data pertaining to Student submissions to assignments (link,description of each submission,
    assignment to which submission each is made, grades given for eachsubmission and list of all submissions
    made by the student).  '''

    def __init__(self,link,description, assignment,grades=[3,2]):
        '''Method that initialize instance of Submission class.'''

        self.link = link
        self.description = description
        self.grades = grades
        self.assignment = assignment
        self.submissions_list = []


    def add_submission_to_submissions_list(self):
        '''Method that creates submission object and appends it to list of all submission object by the given
        instance of student class.'''

        self.submissions_list.append(Submission(self.link,self.description,self.assignment,self.grades))

    def __str__(self):
        '''Method that overwrittes default __str__ method and returns string with basic data taken from instance
        of submission class.'''

        return 'Submission to {} assignment. Link: {}, Description: {}, Grades given: {}'.format(self.assignment,self.link, self.description, self.grades)

