# Author:xichen
# @Time:2019/9/214:05


from core import admin, student, teacher

func_dic = {
    '1': admin.view,
    '2': student.view,
    '3': teacher.view,
}

def run():
    while True:
        print('''

        1.管理员视图
        2.学生视图
        3.老师视图

        ''')

        choice = input('选择视图:')
        if choice == 'q':
            break

        if choice not in func_dic:
            print('输入错误 !')
            continue
        else:
            func_dic[choice]()


if __name__ == '__main__':
    run()