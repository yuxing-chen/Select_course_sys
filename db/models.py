# Author:xichen
# @Time:2019/8/309:28
from db import db_handler

# 所有类的基类
class Base:

    # 调用db_handler的保存数据save方法
    def save(self):
        db_handler.save(self)

    # 类的数据属性
    @classmethod
    def select(cls,username):
        obj = db_handler.select(cls,username)
        return obj





# 管理员类：
class Admin(Base):
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
        self.save()

    # 管理员创建学校方法
    def creat_school(self,school_name,school_addr):
        School(school_name,school_addr)

    # 管理员创建老师方法
    def creat_teacher(self,teacher_name):
        Teacher(teacher_name)

    # 管理员创建课程方法
    def creat_course(self,school_name,course_name):

        # 给学校添加课程
        # 获取学校对象
        school_self  = School.select(school_name)

        # 实例化课程对象
        Course(course_name)

        # 给学校添加课程
        school_self.add_course(course_name)




# 学生类
class Student(Base):
    def __init__(self,student_name,student_pwd):
        self.name = student_name
        self.pwd = student_pwd
        self.school = None
        self.course_list = []
        self.score = {}
        self.save()


    # 学生选择学校方法
    def choose_school(self,school_name):
        self.school = school_name
        self.save()

    # 学生选择课程方法
    def choose_course(self,course_name):
        self.course_list.append(course_name)
        self.score[course_name] = 0
        self.save()

        # 让课程也选择学生
        course_self = Course.select(course_name)
        course_self.add_student(self.name)

    def check_score(self,course_name):
        return self.score[course_name]






# 学校类
class School(Base):
    def __init__(self,school_name,school_addr):
        self.name = school_name
        self.addr =school_addr
        self.course_list = []
        self.save()

    # 学校添加课程的方法
    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save()





# 老师类
class Teacher(Base):
    def __init__(self,teacher_name,teacher_pwd ='456'):
        self.name = teacher_name
        self.pwd = teacher_pwd
        self.course_list =[]
        self.save()

    # 老师添加教授课程方法
    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save()

    # 老师查看教授课程下的学生方法
    def check_student(self,course_name):
        course_self = Course.select(course_name)
        return  course_self.student_list

    # 老师修改学生的成绩
    def change_score(self,course_name,student_name,score):
        student_self = Student.select(student_name)
        student_self.score[course_name] = score
        student_self.save()






# 课程类
class Course(Base):
    def __init__(self,course_name):
        self.name = course_name
        self.student_list = []
        self.save()

    def add_student(self,student_name):
        self.student_list.append(student_name)
        self.save()