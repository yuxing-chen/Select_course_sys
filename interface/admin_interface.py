# Author:xichen
# @Time:2019/8/309:28
from db import models

# 管理员注册接口
def register_interface(username,pwd):

    admin_self = models.Admin.select(username)
    if admin_self:
        return False,'用户已经存在'

    models.Admin(username,pwd)
    return True,'用户创建成功'


# 管理员登录接口
def login_interface(username,pwd):
    admin_self = models.Admin.select(username)
    if admin_self:
        if admin_self.pwd == pwd:
            return True,f'管理员{username}登录成功'
        else:
            return False,f'管理员{username}密码错误'

    else:
        return False,f'管理员{username}不存在'


# 管理员创建学校接口
def school_interface(admin_name,school_name,school_addr):
    school_self = models.School.select(school_name)
    if school_self:
        return False,f'学校{school_name}已存在，重新输入学校名'

    admin_self = models.Admin.select(admin_name)
    admin_self.creat_school(school_name,school_addr)
    return True,f'学校{school_name}创建成功'


# 管理员创建老师接口
def teacher_interface(admin_name,teacher_name):
    teacher_self = models.Teacher.select(teacher_name)
    if teacher_self:
        return False,f'老师{teacher_name}已存在,重新输入'

    admin_self = models.Admin.select(admin_name)
    admin_self.creat_teacher(teacher_name)
    return True,f'老师{teacher_name}创建成功'


# 管理员创建课程接口
def course_interface(admin_name,school_name,course_name):
    # 读取管理员选择的学校
    school_self = models.School.select(school_name)
    # 判断管理员创建的课程名是否存在该学校
    if course_name in school_self.course_list:
        return False,f'课程{course_name}已存在'

    admin_self = models.Admin.select(admin_name)
    admin_self.creat_course(school_name,course_name)
    return True,f'课程{course_name}已加入{school_name}学校'
