# Author:xichen
# @Time:2019/9/123:41

from db import db_handlers


class Base:
    def save(self):
        db_handlers.save(self)

    @classmethod
    def select(cls, name):
        self = db_handlers.select(cls, name)
        return self


class Admin(Base):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.save()

    def creat_school(self, name, addr):
        School(name, addr)

    def creat_teacher(self, name):
        Teacher(name)

    def creat_course(self, school, course):
        Course(course)

        school_self = School.select(school)
        school_self.add_course(course)


class Teacher(Base):
    def __init__(self, name, pwd='456'):
        self.name = name
        self.pwd = pwd
        self.course_list = []
        self.save()

    def choose_course(self,name):
        self.course_list.append(name)
        self.save()

    def check_student(self,name):
        course_self = Course.select(name)
        return course_self.student_list

    def change_score(self, student, course, score):
        student_self = Student.select(student)
        student_self.score[course] = score
        student_self.save()


class School(Base):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.course_list = []
        self.save()

    def add_course(self, course):
        self.course_list.append(course)
        self.save()


class Course(Base):
    def __init__(self, name):
        self.name = name
        self.student_list = []
        self.save()

    def add_student(self, name):
        self.student_list.append(name)
        self.save()


class Student(Base):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd
        self.school = None
        self.course_list = []
        self.score = {}
        self.save()

    def choose_school(self, name):
        self.school = name
        self.save()

    def choose_course(self, course_name):
        self.course_list.append(course_name)
        self.score[course_name] = 0
        self.save()

        course_self = Course.select(course_name)
        course_self.add_student(self.name)

    def check_score(self, name):
        return self.score[name]

