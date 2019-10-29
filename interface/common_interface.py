# Author:xichen
# @Time:2019/9/214:29

import  os
from conf import settings

def get_school_interface():
    school_path = os.path.join(settings.DB_PATH,'School')
    if os.path.isdir(school_path):
        school_list = os.listdir(school_path)
        return True,school_list
    else:
        return False,'还没有学校信息'
    
    
    
    
def get_course_interface():
    course_path = os.path.join(settings.DB_PATH,'Course')
    if os.path.isdir(course_path):
        course_list = os.listdir(course_path)
        return True,course_list
    else:
        return False,'还没有学校信息'