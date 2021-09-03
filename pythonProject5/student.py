import re
import sys


class Student():

    def __init__(self, name, surname, birthday, sex, current_mark, speciality, course):
        try:
            if re.match("[A-Z][a-z]+", name):
                self.__name = name
            else:
                raise ValueError
        except ValueError:
            print('ERROR')
            print("Name should be string and start by upper case")
            sys.exit(1)

        try:
            if re.match("[A-Z][a-z]+", surname):
                self.__surname = surname
            else:
                raise ValueError
        except ValueError:
            print('ERROR')
            print("Surname should be string and start by upper case")
            sys.exit(1)

        try:
            if re.match("(([0-2]\d|[3][0-1])\.([0][1-9]|[1][0-2])\.(19[0-9]{2}|20[0-1]\d))", birthday):
                self.__birthday = birthday
            else:
                raise ValueError
        except ValueError:
            print('ERROR')
            print("Birthday should be DD.MM.YYYY")
            sys.exit(1)

        try:
            if re.match("Male|Female",sex):
                self.__sex = sex
            else:
                raise ValueError
        except ValueError:
            print('ERROR')
            print("Sex should be Male or Female")
            sys.exit(1)

        try:
            if current_mark in range(0, 11):
                self.__current_mark = current_mark
            else:
                raise ValueError
        except ValueError:
            print('ERROR')
            print("Mark should be number between 1 and 10")
            sys.exit(1)

        try:
            if re.match("[a-zA-Z]{1,50}", speciality):
                self.__speciality = speciality
            else:
                raise ValueError
        except ValueError:
            print('ERROR')
            print("Speciality should be string less then 50 characters")

        try:
            if course in range(1, 9):
                self.__course = course
            else:
                raise ValueError
        except ValueError:
            print('ERROR')
            print("Course should be number")

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def birthday(self):
        return self.__birthday

    @property
    def sex(self):
        return self.__sex

    @property
    def current_mark(self):
        return self.__current_mark

    @current_mark.setter
    def current_mark(self, new):
        try:
            if new in range(0, 11):
                self.__current_mark = new
            else:
                raise ValueError
        except ValueError:
            print('ERROR')
            print("Mark should be number between 1 and 10")


    @property
    def speciality(self):
        return self.__speciality

    @speciality.setter
    def speciality(self, new):
        try:
            if re.match("[a-zA-Z]{1,50}", new):
                self.__speciality = new
            else:
                raise ValueError
        except ValueError:
            print('ERROR')
            print("Speciality should be string less then 50 characters")

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, new):
        try:
            if new in range(1, 9):
                self.__course = new
            else:
                raise ValueError
        except ValueError:
            print('ERROR')
            print("Course should be number")

a = Student('Grzegorz', 'Brzęczyszczykiewicz', '01.09.1939', 'Male', 5, 'Canonier', 4)

