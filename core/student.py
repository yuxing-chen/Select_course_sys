# Author:xichen
# @Time:2019/9/214:26

# Author:xichen
# @Time:2019/9/117:17
from interface import student_interface
from interface import common_interface
from lib import common

student_info = {'user': None}


def register(): 
    while True:
        name = input('输入学生用户名：')
        if name  =='q':
            break
        pwd = input('输入学生密码：')
        re_pwd = input('确认学生密码：')
        if re_pwd == pwd:
            flag,msg = student_interface.register_interface(name,pwd)
            print(msg)
            if flag:
                break
        else:
            print('两次密码不一样 ！')


def login(): 
    while True:
        name = input('输入学生用户名：')
        if name  =='q':
            break
        pwd = input('输入学生密码：')
        flag,msg = student_interface.login_interface(name,pwd)
        print(msg)
        if flag:
            student_info['user'] = name
            break


@common.login_auth('student')
def choose_school():
    while True:
        flag, school_list = common_interface.get_school_interface()
        if not flag:
            print(school_list)
            break
        else:
            for i, school in enumerate(school_list):
                print(f'{i}:{school}')
            choice = input('选择学校编号：')
            if choice == 'q':
                break
            if not choice.isdigit():
                print('必须是数字 !')
                continue

            choice = int(choice)
            if choice not in range(len(school_list)):
                print('没有这个学校！')
                continue
            school_name = school_list[choice]
            flag,msg = student_interface.choose_school_interface(student_info['user'],school_name)
            print(msg)
            break


@common.login_auth('student')
def choose_course():
    while True:
        flag,course_list = student_interface.get_student_school(student_info['user'])
        if not flag:
            print(course_list)
            break
        else:
            for i, course in enumerate(course_list):
                print(f'{i}:{course}')
            choice = input('选择学校编号：')
            if choice == 'q':
                break
            if not choice.isdigit():
                print('必须是数字 !')
                continue

            choice = int(choice)
            if choice not in range(len(course_list)):
                print('没有这个学校！')
                continue
            course_name = course_list[choice]
            flag,msg = student_interface.choose_course_interface(student_info['user'],course_name)
            print(msg)
            break
            
        



@common.login_auth('student')
def check_score():
    while True:
        flag, course_list = student_interface.get_student_course(student_info['user'])
        if not flag:
            print(course_list)
            break
        else:
            for i, course in enumerate(course_list):
                print(f'{i}:{course}')
            choice = input('选择学校编号：')
            if choice == 'q':
                break
            if not choice.isdigit():
                print('必须是数字 !')
                continue

            choice = int(choice)
            if choice not in range(len(course_list)):
                print('没有这个学校！')
                continue
            course_name = course_list[choice]
            flag, msg = student_interface.check_score_interface(student_info['user'], course_name)
            print(msg)
            break
    








func_dic = {
    '1': register,
    '2': login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score,

}


def view():
    while True:
        print('''

        1、注册
        2、登录
        3、选择校区
        4、选择课程
        5、查看成绩

        ''')

        choice = input('选择学生功能:')
        if choice == 'q':
            break

        if choice not in func_dic:
            print('输入错误 !')
            continue
        else:
            func_dic[choice]()
