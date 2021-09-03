import json
from datetime import datetime
import re
import string
import random
from extended_student import ExtendedStudent

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits


def combine_pass():
    password = ''
    length = random.randint(6, 9)
    for i in range(length):
        password += random.choice(alphabet)
    return password


def combine_login(name, surname):
    return name[0].lower() + surname.lower()


class StudentsCreds():
    students_filename = "students.dat"
    ext_students_filename = "ext_students.dat"

    students_file = open(students_filename, mode='r', encoding='utf-8-sig')
    ext_students_file = open(ext_students_filename, mode='w', encoding='utf_8')

    students = students_file.readlines()
    ext_students = []


    for line in students:
        student = line.strip().split(':::')
        birthday = datetime.strptime(student[2], "%Y-%m-%d")
        student[2] = birthday.strftime("%d.%m.%Y")
        if student[3] == 'M':
            student[3] = "Male"
        elif student[3] == 'F':
            student[3] = "Female"
        student[4] = int(student[4])
        student[6] = int(student[6])
        print(student)
        ext_students.append(ExtendedStudent(*student, combine_login(student[0], student[1]), combine_pass()))


        for i in range(len(ext_students)):
            ext_students_file.write(ext_students[i].name + '\t' + ext_students[i].surname + '\t' + ext_students[i].birthday + '\t' + ext_students[i].sex + '\t' + str(ext_students[i].course) + '\t' + ext_students[i].speciality+'\t' + str(ext_students[i].current_mark) + '\t' + ext_students[i].login + ':' + ext_students[i].password + '\n')


