class Assignment:
    '''Assignment class containing data pertaining to assignment created by Mentor.'''

    ASSIGNMENT_SUBMISSION = {}

    def __init__(self, name_assignment, deadline, date_added,task):
        self.name_assignment = name_assignment
        self.deadline = deadline
        self.date_added = date_added
        self.task = task

        self.ASSIGNMENT_SUBMISSION[self] = None

    def __str__(self):


        return 'Assignment: {}; Task: {}; Deadline: {}; Added: {}.}'.format(self.name_assignment, self.task, self.deadline, self.date_added)

    # def to_list(self):
    #     '''Method that extracts data from Assigment class and converts it into string.'''
    #
    #
    #     string_grades_criteria = ''
    #
    #     for criteria in range(len(grades_criteria)):
    #
    #         if criteria == len(grades_criteria)-1:
    #             string_grades_criteria += grades_criteria[criteria]
    #
    #         else:
    #             string_grades_criteria += grades_criteria[criteria] + ','
    #
    #     string_submission_grades = ''
    #
    #     for index in range(len(self.ASSIGNMENT_SUBMISSION[self].grades)):
    #         if index == len(self.ASSIGNMENT_SUBMISSION[self].grades) - 1:
    #             string_submission_grades += self.ASSIGNMENT_SUBMISSION[self].grades[index]
    #
    #         else:
    #             string_submission_grades += self.ASSIGNMENT_SUBMISSION[self].grades[index] + ','
    #     # submission_data = ''
    #     # assignment_data = ''
    #     # for assignment in self.ASSIGNMENT_SUBMISSION:
    #     #     assignment_data += assignment.name_assignment + ',' + assignment.deadline + ',' assignment.date_added + ',' + strassignment.grades_criteria + ',' + assignment.task
    #     #     submission_data += self.ASSIGNMENT_SUBMISSION.link + ',' + self.ASSIGNMENT_SUBMISSION.description +
    #     #
    #     # submissions = []
    #     #
    #     # if self.submissions:
    #     #     for submission in self.submissions.submissions_list:
    #     #         submission_data = [submission.link, submission.description, str(submission.grades), submission.assignment.name_assignment, submission.assignment.deadline, submission.assignment.date_added, str(submission.assignment.grades_criteria), submission.assignment.task]
    #     #         submissions.append(submission_data)
    #
    #     return [self.name_assignment, self.deadline, self.date_added, grades_criteria, self.task, ASSIGNMENT_SUBMISSION[self].link, ASSIGNMENT_SUBMISSION[self].description, string_submission_grades]
    #
    #
    # @classmethod
    # def write_changes_to_file(cls, filename):
    #     '''Saves data extracted from instances of Student class (by to_list method) into given file.'''
    #
    #     with open(filename, "w") as class_file:
    #         for assignment in self.ASSIGNMENT_SUBMISSION:
    #
    #             row = ",".join(obj.to_list())
    #
    #             class_file.write(row + "\n")
    #         class_file.close()
    #
    # @classmethod
    # def loading_file(cls, filename):
    #     '''Method that loads data from file and creats objects of assigment class'''
    #
    #     with open(filename, 'r') as class_file:
    #
    #         for line in class_file:
    #
    #             line_splitted = line.strip('\n').split(',')
    #
    #
    #
    #
    #                 one_from_students = Student(line_splitted[0], line_splitted[1], int(line_splitted[2]),
    #                                             line_splitted[3],
    #                                             line_splitted[4], line_splitted[5], line_splitted[6], line_splitted[7],
    #                                             line_splitted[8])
    #
    #                 try:  # to check whether there is submission data
    #
    #                     assignment_submitted = Assignment(line_splitted[14], line_splitted[15], line_splitted[16],
    #                                                       line_splitted[17], line_splitted[18])
    #                     one_from_students.submit_submission(line_splitted[11], line_splitted[12], assignment_submitted,
    #                                                         line_splitted[13])  # creating instance of Submission class
    #
    #
    #                 except IndexError:
    #                     pass  # if there are no submission data then instance of student object is created without instances of submission class
    #
    #                 try:  # to check whether there is attendance data
    #                     attendance_dates_status = line_splitted[10].split('|')
    #
    #                     separated_dates_status = []
    #                     for item in attendance_dates_status:
    #                         separated_dates_status.append(item.split(':'))
    #
    #                     for element in range(len(separated_dates_status)):
    #                         one_from_students.list_of_attendance.checking_presence(separated_dates_status[element][0],
    #                                                                                int(separated_dates_status[element][
    #                                                                                        1]))  # creating instances of Attendance class
    #
    #                 except IndexError:
    #                     pass  # if there are no attendance data then instance of student object is created without instances of attendance class
    #
    #             class_file.close()
    #

#
#
# print(To_do_list)









