from student import Student


class ExtendedStudent(Student):
    def __init__ (self, name, surname, birthday, sex, current_mark, speciality, course, login, password):
        super().__init__(name, surname, birthday, sex, current_mark, speciality, course)
        self.__login = login
        self.__password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password