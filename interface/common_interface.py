# Author:xichen
# @Time:2019/8/309:28

import os
from conf import settings

# 获取所有学校列表
def get_school_list():
    # 获取学校对象的文件夹路径
    school_path = os.path.join(settings.DB_PATH,'School')
    
    # 判断保存学校对象的文件夹是否存在
    if os.path.isdir(school_path):
        school_list = os.listdir(school_path)
        return school_list


# 获得所有课程接口
def get_course_list():
    course_path = os.path.join(settings.DB_PATH,'Course')
    if os.path.isdir(course_path):
        course_list  = os.listdir(course_path)
        return course_list
