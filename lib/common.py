# Author:xichen
# @Time:2019/9/214:06



def login_auth(type):
    def auth(func):
        from core import admin,student,teacher
        def inner(*args,**kwargs):
            if type == 'admin':
                if admin.admin_info.get('user'):
                    res =func(*args,**kwargs)
                    return  res
                else:
                    admin.login()
            elif type == 'student':
                if student.student_info.get('user'):
                    res =func(*args,**kwargs)
                    return  res
                else:
                    student.login()

            elif type == 'teacher':
                if teacher.teacher_info.get('user'):
                    res =func(*args,**kwargs)
                    return  res
                else:
                    teacher.login()


        return  inner

    return auth