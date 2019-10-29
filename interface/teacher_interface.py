# Author:xichen
# @Time:2019/9/214:27


from db import modlers


def login_interface(name,pwd):
    self = modlers.Teacher.select(name)
    if self:
        if self.pwd == pwd:
            return True,'用户登录成功'
        else:
            return False,'用户密码错误 ！'
    else:
        return False,'用户不存在 ！'
    
def check_course_interface(name):
    self = modlers.Teacher.select(name)
    course_list = self.course_list
    if course_list:
        return True,course_list
    else:
        return False,'你还没有选择课程 ！'
    
def choose_course_interface(name,course_name):
    self = modlers.Teacher.select(name)
    course_list = self.course_list
    if course_name in course_list:
        return False,'课程已经存在你的课程列表，不能重复选！'
    else:
        self.choose_course(course_name)
        return True,'课程已经添加成功 '
    
    
def check_student_interface(name,course_name):
    self = modlers.Teacher.select(name)
    student_list = self.check_student(course_name)
    print(student_list)
    if student_list:
        return True,student_list
    else:
        return False,'这门课程下暂时没有学生信息 ！'
    
def change_score_interface(name,student_name,course_name,score):
    self = modlers.Teacher.select(name)
    self.change_score(student_name,course_name,score)
    return True,'该学生的成绩修改成功'
    
    