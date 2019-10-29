# Author:xichen
# @Time:2019/9/214:27

from db import modlers

def register_interface(name,pwd):
    self = modlers.Student.select(name)
    if self:
        return False,'用户已存在，不可创建 ！'
    else:
        modlers.Student(name,pwd)
        return True,'用户创建成功'

def login_interface(name,pwd):
    self = modlers.Student.select(name)
    if self:
        if self.pwd == pwd:
            return True,'用户登录成功'
        else:
            return False,'用户密码错误 ！'
    else:
        return False,'用户不存在 ！'

def choose_school_interface(name,school_name):
    self = modlers.Student.select(name)
    school = self.school
    if school is None:
        self.choose_school(school_name)
        return True,'学校选择成功'
    else:
        return False,'你已经选择过学校，不能重复选择 ！'


def get_student_school(name):
    self = modlers.Student.select(name)
    school = self.school
    if school is None:
        return  False,'你还没有选择学校'
    else:
        school_self = modlers.School.select(school)
        course_list = school_self.course_list
        if course_list:
            return True,course_list
        else:
            return False,'你选择的学校，还没有课程信息！'
def choose_course_interface(name,course_name):
    self = modlers.Student.select(name)
    course_list = self.course_list
    if course_name in course_list:
        return False,'选择课程失败，该课程已存在 ！'
    else:
        self.choose_course(course_name)
        return True,'课程已经添加你的课程列表'
    
def get_student_course(name):
    self = modlers.Student.select(name)
    course_list = self.course_list
    if course_list:
        return True,course_list
    else:
        return False,'你还没有选择课程 ！'
def check_score_interface(name,course_name):
    self = modlers.Student.select(name)
    score = self.check_score(course_name)
    return  True,f'{course_name}:{score}'