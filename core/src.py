# Author:xichen
# @Time:2019/8/309:27
from core import admin,student,teacher




func_dic = {
    '1':admin.admin_view,
    '2':student.student_view,
    '3':teacher.teacher_view,
}
def run():
    while True:
        print('''
        1:管理员视图
        2:学生视图
        3:老师视图
        q:退出
        ''')

        choice = input('选择视图:')
        if choice =='q':
            break

        if not func_dic.get(choice):
            print('没有该视图')
            continue
        func_dic.get(choice)()


if __name__ == '__main__':
    run()