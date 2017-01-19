from employee import Employee
def get_from_object_to_list(list_of_obj):
    list_of_all = []
    for persons in list_of_obj:
        list = []
        list = [persons.name, persons.surname, persons.age, persons.gender, persons.pesel, persons.login, persons.status, persons.date_when_added]
        list_of_all.append(list)
    return list_of_all
def print_table(table, title_list):
    """
    Prints table with data. Sample output:
        /-----------------------------------\
        |   id   |      title     |   type  |
        |--------|----------------|---------|
        |   0    | Counter strike |   fps   |
        |--------|----------------|---------|
        |   1    |       fo       |   fps   |
        \-----------------------------------/
    Args:
        table: list of lists - table to display
        title_list: list containing table headers
    Returns:
        This function doesn't return anything it only prints to console.
    """
    table.insert(0, title_list)
    width_list = []
    for i in range(len(table[0])):
        longest_string = 0
        for row in table:
            if len(row[i]) > longest_string:
                longest_string = len(row[i])
        width_list.append(longest_string)
    print("╔", end="")
    for column in range(len(table[0])):
        print("{0:═^{w}}".format("═", w=width_list[column]+2), end="")
        if column+1 != len(table[0]):
            print("╦", end="")
    print("╗\n", end="")
    '''content'''
    for row_number, row in enumerate(table):
        for column, cell in enumerate(row):
            print("║{0:^{w}}".format(cell, w=width_list[column]+2), end="")
        print("║\n", end="")
        if row_number+1 != len(table):
            print("╠", end="")
            for column, cell in enumerate(row):
                print("{0:═^{w}}".format("═", w=width_list[column]+2), end="")
                if column+1 != len(table[0]):
                    print("╬", end="")
            print("╣\n", end="")
        '''footer'''
        if row_number+1 == len(table):
            print("╚", end="")
            for column, cell in enumerate(row):
                print("{0:═^{w}}".format("═", w=width_list[column]+2), end="")
                if column+1 != len(table[0]):
                    print("╩", end="")
            print("╝")
    table.remove(table[0])
# Employee.loading_file()
# head =["name","surname","age","gender","pesel","login","status", "date_added"]
# print_table(get_from_object_to_list(Employee.get_all()),head)