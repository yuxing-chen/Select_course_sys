# Author:xichen
# @Time:2019/8/309:27


from interface import teacher_interface
from interface import common_interface
from lib import common

teacher_info = {'user':None}

# 老师登录功能
def login():
    while True:
        username = input('输入老师用户名：')
        if username == 'q':
            break
        pwd = input('输入密码：')
        flag,msg = teacher_interface.login_interface(username,pwd)
        if flag:
            print(msg)
            teacher_info['user'] = username
            break
        else:
            print(msg)




# 老师查看教授课程功能
@common.login_auth('teacher')
def check_course():
    flag,course_msg = teacher_interface.check_course(teacher_info['user'])
    if flag:
        print(course_msg)
    else:
        print(course_msg)


# 老师选择课程功能
@common.login_auth('teacher')
def choose_course():
    while True:
        course_list = common_interface.get_course_list()
        if  not course_list:
            print('暂时没有可选课程！')
            break
        else:
            for i,course in enumerate(course_list):
                print(f'{i}:{course}')
            choice = input('选择课程')
            if choice == 'q':
                break

            if not choice.isdigit():
                print('必须是数字！')
                continue

            choice = int(choice)
            if choice not in range(len(course_list)):
                print('没有这个课程！')
                continue

            course_name = course_list[choice]
            flag,msg = teacher_interface.choose_course(teacher_info['user'],course_name)
            if flag:
                print(msg)
                break
            else:
                print(msg)


# 老师查看课程下的学生功能
@common.login_auth('teacher')
def check_course_student():
    while True:
        flag, course_list= teacher_interface.check_course(teacher_info['user'])
        if not flag:
            print(course_list)
            break

        for i, course in enumerate(course_list):
            print(f'{i}:{course}')
        choice = input('选择查看的课程')
        if choice == 'q':
            break

        if not choice.isdigit():
            print('必须是数字！')
            continue

        choice = int(choice)
        if choice not in range(len(course_list)):
            print('没有这个课程！')
            continue

        course_name = course_list[choice]
        flag,student_list = teacher_interface.check_course_student_interface(teacher_info['user'],course_name)
        if flag:
            print(f'选择该课程的学生为：{student_list}')
            break
        else:
            print(student_list)



# 老师修改学生成绩功能
@common.login_auth('teacher')
def change_score():
    while True:
        # 获得该老师自己的所有教授的课程
        flag, course_list= teacher_interface.check_course(teacher_info['user'])
        if not flag:
            print(course_list)
            break

        for i, course in enumerate(course_list):
            print(f'{i}:{course}')
        choice = input('选择需要修改学生成绩所在的课程')
        if choice == 'q':
            break

        if not choice.isdigit():
            print('必须是数字！')
            continue

        choice = int(choice)
        if choice not in range(len(course_list)):
            print('没有这个课程！')
            continue

        course_name = course_list[choice]

        # 查看该老师选择的课程下的所有学生
        flag,student_list = teacher_interface.check_course_student_interface(teacher_info['user'],course_name)
        if not flag:
            print('该课程没有学生！')
            continue
        else:
            for i, course in enumerate(student_list):
                print(f'{i}:{course}')
            choice1 = input('选择需要修改学生成绩')
            if choice1 == 'q':
                break

            if not choice1.isdigit():
                print('必须是数字！')
                continue

            choice1 = int(choice1)
            if choice1 not in range(len(student_list)):
                print('没有这个学生')
                continue

            studnet_name = student_list[choice1]
            score = input('输入修改的成绩：')
            if not score.isdigit():
                print('必须是数字！')
                continue

            flag,msg = teacher_interface.change_score_interface(teacher_info['user'],course_name,studnet_name,score)
            if flag:
                print(msg)













func_dic = {
   '1':login,
   '2':check_course,
   '3':choose_course,
   '4':check_course_student,
   '5':change_score,
}
def teacher_view():
    while True:
        print('''
        1、登录
        2、查看教授课程
        3、选择教授课程
        4、查看课程下学生
        5、修改学生成绩
        ''')
        choice = input('选择老师功能：')
        if choice == 'q':
            break
        if not func_dic.get(choice):
            print('功能不存在')
            continue

        func_dic.get(choice)()

