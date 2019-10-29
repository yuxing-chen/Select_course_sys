# Author:xichen
# @Time:2019/9/214:27


from interface import teacher_interface
from interface import common_interface
from lib import common

teacher_info = {'user': None}


def login(): 
    while True:
        name = input('输入老师用户名：')
        if name  =='q':
            break
        pwd = input('输入老师密码：')
        flag,msg = teacher_interface.login_interface(name,pwd)
        print(msg)
        if flag:
            teacher_info['user'] = name
            break


@common.login_auth('teacher')
def check_course():
    flag,msg = teacher_interface.check_course_interface(teacher_info['user'])
    print(msg)


@common.login_auth('teacher')
def choose_course():
    while True:
        flag, course_list = common_interface.get_course_interface()
        if not flag:
            print(course_list)
            break
        else:
            for i, course in enumerate(course_list):
                print(f'{i}:{course}')
            choice = input('选择课程编号：')
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
            flag,msg = teacher_interface.choose_course_interface(teacher_info['user'],course_name)
            print(msg)
            if flag:
                break
                


@common.login_auth('teacher')
def check_student():
    while True:
        flag,course_list = teacher_interface.check_course_interface(teacher_info['user'])
        if not flag:
            print(course_list)
            break
        else:
            for i, course in enumerate(course_list):
                print(f'{i}:{course}')
            choice = input('选择课程编号：')
            if choice == 'q':
                break
            if not choice.isdigit():
                print('必须是数字 !')
                continue

            choice = int(choice)
            if choice not in range(len(course_list)):
                print('没有这个课程！')
                continue
            course_name = course_list[choice]
            flag,msg = teacher_interface.check_student_interface(teacher_info['user'],course_name)
            print(msg)
            break
            
                
            
            
        
@common.login_auth('teacher')
def change_score():
    while True:
        flag,course_list = teacher_interface.check_course_interface(teacher_info['user'])
        if not flag:
            print(course_list)
            break
        else:
            for i, course in enumerate(course_list):
                print(f'{i}:{course}')
            choice = input('选课程编号：')
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
            flag,student_list = teacher_interface.check_student_interface(teacher_info['user'],course_name)
            if not flag:
                print(student_list)
                break
            else:
                for i, student in enumerate(student_list):
                    print(f'{i}:{student}')
                choice = input('选择学校编号：')
                if choice == 'q':
                    break
                if not choice.isdigit():
                    print('必须是数字 !')
                    continue

                choice = int(choice)
                if choice not in range(len(student_list)):
                    print('没有这个学校！')
                    continue
                student_name = student_list[choice]
                score = input('输入修改的成绩分数：')
                if int(score) >100 or not score.isdigit():
                    print('成绩输入错误 ！')
                    continue
                flag,msg = teacher_interface.change_score_interface(
                    teacher_info['user'],
                    student_name,
                    course_name,
                    score,
                )
                print(msg)
                if  flag:
                    break
                    
                
    


func_dic = {
    '1': login,
    '2': check_course,
    '3': choose_course,
    '4': check_student,
    '5': change_score,

}


def view():
    while True:
        print('''

        1、登录
        2、查看教授课程
        3、选择教授课程
        4、查看课程下学生
        5、修改学生成绩

        ''')

        choice = input('选择老师功能:')
        if choice == 'q':
            break

        if choice not in func_dic:
            print('输入错误 !')
            continue
        else:
            func_dic[choice]()