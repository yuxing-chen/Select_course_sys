# Author:xichen
# @Time:2019/8/309:28

from db import models

# 学生注册接口
def register_interface(username,pwd):
    student_self = models.Student.select(username)
    if student_self:
        return False,f'学生{username}已经存在'

    models.Student(username,pwd)
    return True,f'学生{username}注册成功'


# 学生登录接口
def login_interface(username,pwd):
    student_self = models.Student.select(username)
    if student_self:
        if student_self.pwd == pwd:
            return True,f'学生{username}登录成功'
        else:
            return False,f'学生{username}密码错误'

    return False,f'学生{username}未注册'


# 学生选择学校接口
def choose_school_interface(school_name,student_name):
    student_self = models.Student.select(student_name)
    if student_self.school is not None:
        return False,f'学生{student_name}不能重复选择学校！'
    else:
        student_self.choose_school(school_name)
        return True,f'学生{student_name}选择学校成功'



# 学生得到学校下的课程接口
def get_course_interface(student_name):
    student_self = models.Student.select(student_name)
    student_school = student_self.school

    if student_school is not None:
        student_school_self = models.School.select(student_school)
        school_course_list = student_school_self.course_list
        return True,school_course_list
    else:
        return False,f'学生{student_name}还未选择学校'

# 学生选择课程接口
def choose_course_interface(student_name,course_name):

    student_self = models.Student.select(student_name)
    course_list = student_self.course_list
    if course_name in course_list:
        return False,f'该课程已经存在，不得再选'

    student_self.choose_course(course_name)
    return True,f'添加课程成功：{student_self.course_list}'




# 得到学生的所有课程
def get_student_coursr_interface(student_name):
    student_self = models.Student.select(student_name)
    course_list = student_self.course_list
    if course_list:
        return True,course_list
    else:
        return False,f'该学生还未选择课程'

# 学生查看成绩接口
def check_score_interface(student_name,course_name):
    student_self = models.Student.select(student_name)

    student_score = student_self.check_score(course_name)
    return True,f'{course_name}:{student_score}'




