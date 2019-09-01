# Author:xichen
# @Time:2019/8/309:27

from interface import admin_interface
from interface import common_interface
from lib import common

# 管理员登录标识
admin_info = {'user':None}

# 管理员注册功能
def admin_register():
    while True:
        username = input('输入管理员用户名：')
        if username == 'q':
            break
        password = input('输入密码：')
        re_passwprd= input('确认密码：')
        if re_passwprd == password:
            flag,msg = admin_interface.register_interface(username,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
                break
        else:
            print('两次密码不一样。')


# 管理员登录功能
def admin_login():
    while True:
        username = input('输入登录用户名：')
        if username == 'q':
            break
        pwd =input('输入登陆密码：')
        flag,msg = admin_interface.login_interface(username,pwd)
        if flag:
            print(msg)
            admin_info['user'] = username
            break
        else:
            print(msg)



# 管理员创建学校
@common.login_auth('admin')
def create_school():
    while True:
        school_name = input('输入学校名：')
        if school_name == 'q':
            break
        school_addr = input('学校地址：')
        flag,msg = admin_interface.school_interface(admin_info['user'],school_name,school_addr)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 管理员创建老师
@common.login_auth('admin')
def create_teacher():
    while True:
        teacher_name = input('输入老师名字:')
        if teacher_name == 'q':
            break
        flag,msg = admin_interface.teacher_interface(admin_info['user'],teacher_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 管理员创建课程
@common.login_auth('admin')
def create_course():
    while True:
        # 获取所有学校对象列表
        school_list = common_interface.get_school_list()

        # 判断学校对象列表是否存在
        if school_list:
            for i,school in enumerate(school_list):
                print(f'{i}:{school}')
        else:
            print('还没有学校信息')
            break

        # 选择学校添加课程
        choice = input('选择学校添加课程：')
        if choice == 'q':
            break

        if not choice.isdigit():
            print('必须是数字！')
            continue



        choice = int(choice)
        if choice not in range(len(school_list)):
            print('没有这个学校！')
            continue

        # 获取学校名字
        school_name = school_list[choice]
        course_name = input('输入课程名：')
        if course_name == 'q':
            break

        flag,msg = admin_interface.course_interface(admin_info['user'],school_name,course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)





func_dic = {
    '1':admin_register,
    '2':admin_login,
    '3':create_school,
    '4':create_teacher,
    '5':create_course,
}
def admin_view():
    while True:
        print('''
            1、注册
            2、登录
            3、创建学校
            4、创建老师
            5、创建课程
        ''')
        choice = input('选择功能：')
        if choice == 'q':
            break

        if not func_dic.get(choice):
            print('没有该功能。')
            continue

        func_dic.get(choice)()