# Author:xichen
# @Time:2019/8/309:28
#
from db import models
from conf import settings
import  os

# 老师登录接口
def login_interface(teacher_name,pwd):
    teacher_self = models.Teacher.select(teacher_name)
    if teacher_self:
        if teacher_self.pwd == pwd:
            return True,f'{teacher_name}登录成功'
        else:
            return False,f'密码错误'
    else:
        return False,f'该老师不存在'


# 老师查看教授课程功能
def check_course(teacher_name):
    teacher_self = models.Teacher.select(teacher_name)
    if not teacher_self.course_list:
        return False,f'该老师还没有选择教授的课程'
    else:
        return True,teacher_self.course_list




# 老师选择教授课程功能
def choose_course(teacher_name,course_name):
    teacher_self = models.Teacher.select(teacher_name)
    if course_name in teacher_self.course_list:
        return False,f'不得重复选择课程'

    teacher_self.add_course(course_name)
    return  True,f'课程添加成功'


# 老师查看课程下的所有学生功能
def check_course_student_interface(teacher_name,course_name):
    teacher_self = models.Teacher.select(teacher_name)
    student_list = teacher_self.check_student(course_name)
    if student_list:
        return True,student_list
    else:
        return False,'该课程还没有学生选择'


# 老师修改学生成绩功能接口
def change_score_interface(teacher_name,course_name,student_name,score):
    teacher_self = models.Teacher.select(teacher_name)
    teacher_self.change_score(course_name,student_name,score)
    return True,'成绩修改成功'





