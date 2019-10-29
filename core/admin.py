# Author:xichen
# @Time:2019/9/214:25

from interface import admin_interface
from interface import common_interface
from lib import common

admin_info = {'user': None}



def register(): 
    while True:
        name = input('输入管理员用户名：')
        if name  =='q':
            break
        pwd = input('输入管理员密码：')
        re_pwd = input('确认管理员密码：')
        if re_pwd == pwd:
            flag,msg = admin_interface.register_interface(name,pwd)
            print(msg)
            if flag:
                break
        else:
            print('两次密码不一样 ！')
            


def login(): 
    while True:
        name = input('输入管理员用户名：')
        if name  =='q':
            break
        pwd = input('输入管理员密码：')
        flag,msg = admin_interface.login_interface(name,pwd)
        print(msg)
        if flag:
            admin_info['user'] = name
            break
        
    
@common.login_auth('admin')
def creat_school():
    while True:
        name = input('输入学校名：')
        if name == 'q':
            break
        addr = input('输入学校地址：')
        flag,msg = admin_interface.creat_school_interface(admin_info['user'],name,addr)
        print(msg)
        if flag:
            break
            


@common.login_auth('admin')
def creat_teacher():
    while True:
        name = input('输入老师用户名：')
        if name == 'q':
            break
        flag,msg = admin_interface.create_teacher_interface(admin_info['user'],name)
        print(msg)
        if flag:
            break
            



@common.login_auth('admin')
def creat_course():
    while True:
        flag,school_list = common_interface.get_school_interface()
        if not flag:
            print(school_list)
            break
        else:
            for i,school in enumerate(school_list):
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
            course_name = input('输入课程名：')
            flag,msg = admin_interface.creat_course_interface(admin_info['user'],school_name,course_name)
            print(msg)
            if flag:
                break
                


func_dic = {
    '1': register,
    '2': login,
    '3': creat_school,
    '4': creat_teacher,
    '5': creat_course,
}


def view():
    while True:
        print('''

        1、注册
        2、登录
        3、创建学校
        4、创建老师
        5、创建课程

        ''')

        choice = input('选择管理员功能:')
        if choice == 'q':
            break

        if choice not in func_dic:
            print('输入错误 !')
            continue
        else:
            func_dic[choice]()
