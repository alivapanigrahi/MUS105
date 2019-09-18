def is_palindrome(s):
    reverse = s[::-1]
    if s == reverse:
        return True
    else:
        return False

    pass

def is_in(a, b):
    list(a)
    for i in a:
        if i in b:
            return True
        else:
            return False

def is_set(l):
    if(len(set(l)) == len((l))):
        return True
    else:
        return False

    pass

def str_to_int2(num_string):
    if num_string[0:2] == "0b":
        return int(num_string, 2)
    elif num_string[0:2] == "0o":
        return int(num_string, 8)
    elif num_string[0:2] == "0x":
        return int(num_string, 16)
    elif type(int(num_string)) == int:
        return int(num_string)
    else:
        raise ValueError("unrecognized base")
    
    pass

def nth_element(n, my_list):
    if(n < 0 or n >= len(my_list)):
        raise TypeError("Cannot find nth element of inputs ({}, {})".format(n, my_list))
    else:
        return my_list[n]
    
    pass

class Course:
    """description = "Computation and Music 1"""
    """
    the Course class describes a college course. Each course should contain:
        - a course code as a string (i.e. MUS105)
        - a CRN as an integer (i.e. 43357)
        - a course description as a string (i.e. Computation and Music 1)
        - a roster of students as a list
    check the parameter list for exact names of each of these variables

    the Course class as a whole should have a string that describes what university the course
    is in. this class variable should be called university. It should be initialized to "UIUC"

    the Course class should have one static method declared: print_school(), which is defined in more detail below.

    the Course class should have a few instance methods:
        *add_student, which adds a student to a course by netID
        *remove_student, which does the opposite
        *get_description, which prints out some information about the course.

    below, the class skeleton has been written for you. It is up to you to fill out the static members, and all
    of the functions.
    """

    university = "The University of Illinois at Urbana-Champaign"

    @staticmethod
    def print_school():
        print("The University is: " + Course.university)
        
    def __init__(self, code, crn, description):
        self.code = code
        self.crn = crn
        self.description = description
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

        pass

    def remove_student(self, student):
        if student not in self.roster:
            raise ValueError("student is not enrolled in course")
        else:
            self.roster.remove(student)
    
        pass

    def get_description(self):
        return self.description