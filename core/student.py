# Author:xichen
# @Time:2019/8/309:27

from interface import student_interface
from interface import common_interface
from lib import  common



student_info = {'user':None}

# 学生注册功能
def register():
    while True:
        username = input('输入学生姓名：')
        if username == 'q':
            break
        pwd = input('输入密码：')
        re_pwd= input('确认密码：')
        if re_pwd == pwd:
            flag,msg = student_interface.register_interface(username,pwd)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致！')



# 学生登录功能
def login():
    while True:
        username = input('学生登录用户名：')
        if username == 'q':
            break
        pwd = input('输入学生密码：')
        flag,msg = student_interface.login_interface(username,pwd)
        if flag:
            print(msg)
            student_info['user'] = username
            break
        else:
            print(msg)



# 学生选择学校功能
@common.login_auth('student')
def choose_school():
    while True:
        school_list = common_interface.get_school_list()
        if school_list:
            for i ,school in enumerate(school_list):
                print(f'{i}:{school}')
        else:
            print('还没有学校信息，暂时不能选')
            break

        choice = input('请选择学校：')
        if choice == 'q':
            break
        if not choice.isdigit():
            print('请输入数字！')
            continue
        choice = int(choice)
        if choice not in range(len(school_list)):
            print('没有这个学校！')
            continue

        school_name = school_list[choice]
        flag,msg = student_interface.choose_school_interface(school_name,student_info['user'])
        if flag:
            print(msg)
            break
        else:
            print(msg)







# 学生选择课程功能
@common.login_auth('student')
def choose_course():
    while True:
        # 获取学生下的学校的所有课程
        flag,school_course_list = student_interface.get_course_interface(student_info['user'])

        if flag:
            if school_course_list:
                for i,course in enumerate(school_course_list):
                    print(f'{i}:{course}')
            else:
                print('该学校还没有课程！')
                break


            choice = input('选择课程')
            if choice == 'q':
                break

            if not choice.isdigit():
                print('必须是数字！')
                continue

            choice = int(choice)
            if choice not in range(len(school_course_list)):
                print('没有这个课程！')
                continue

            course_name = school_course_list[choice]
            flag,msg = student_interface.choose_course_interface(student_info['user'],course_name)
            if flag:
                print(msg)
                break
            else:
                print(msg)

        else:
            print(school_course_list)
            break







# 学生查看成绩功能
@common.login_auth('student')
def check_score():
    while True:
        flag,student_course_list = student_interface.get_student_coursr_interface(student_info['user'])
        if not flag:
            print(student_course_list)
            break
        else:
            for i,course in enumerate(student_course_list):
                print(f'{i}:{course}')
            choice = input('选择课程')
            if choice == 'q':
                break

            if not choice.isdigit():
                print('必须是数字！')
                continue

            choice = int(choice)
            if choice not in range(len(student_course_list)):
                print('没有这个课程！')
                continue

            course_name = student_course_list[choice]
            flag,student_score = student_interface.check_score_interface(student_info['user'],course_name)
            if flag:
                print(student_score)
                break
















func_dic = {
    '1':register,
    '2':login,
    '3':choose_school,
    '4':choose_course,
    '5':check_score,
}
def student_view():
    while True:
        print('''
        1、注册
        2、登录
        3、选择校区
        4、选择课程
        5、查看成绩
        ''')

        choice = input('选择学生功能：')
        if choice == 'q':
            break
        if not func_dic.get(choice):
            print('功能不存在')
            continue

        func_dic.get(choice)()
