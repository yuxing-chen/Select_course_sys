# Author:xichen
# @Time:2019/9/214:27

from db import modlers

def register_interface(name,pwd):
    self = modlers.Admin.select(name)
    if self:
        return False,'用户已存在，不可创建 ！'
    else:
        modlers.Admin(name,pwd)
        return True,'用户创建成功'

def login_interface(name,pwd):
    self = modlers.Admin.select(name)
    if self:
        if self.pwd == pwd:
            return True,'用户登录成功'
        else:
            return False,'用户密码错误 ！'
    else:
        return False,'用户不存在 ！'

def creat_school_interface(name,school_name,addr):
    self = modlers.Admin.select(name)
    school_self = modlers.School.select(school_name)
    if school_self:
        return False,'学校创建失败，学校已存在 ！'
    else:
        self.creat_school(school_name,addr)
        return True,'学校创建成功'


def create_teacher_interface(name,teacher_name):
    self = modlers.Admin.select(name)
    teacher_self = modlers.Teacher.select(teacher_name)
    if teacher_self:
        return False, '老师创建失败，老师已存在 ！'
    else:
        self.creat_teacher(teacher_name)
        return True, '老师创建成功'




def creat_course_interface(name,school_name,course_name):
    self = modlers.Admin.select(name)
    school_self = modlers.School.select(school_name)
    course_list = school_self.course_list
    if course_name in course_list:
        return False,'该课程已存在，不能重复创建 ！'
    else:
        self.creat_course(school_name,course_name)
        return True,'该课程已经成功添加至学校'

