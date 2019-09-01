# Author:xichen
# @Time:2019/8/309:29


def login_auth(type):
    def auth(func):
        from core import admin,teacher,student
        def inner(*args,**kwags):
            if type == 'admin':
                if admin.admin_info.get('user'):
                    res = func(*args,**kwags)
                    return res
                else:
                    admin.admin_login()


            elif type == 'student':
                if student.student_info.get('user'):
                    res = func(*args,**kwags)
                    return res
                else:
                    student.login()


            elif type == 'teacher':
                if teacher.teacher_info.get('user'):
                    res = func(*args,**kwags)
                    return res
                else:
                    teacher.login()


        return inner
    return auth