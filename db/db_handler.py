# Author:xichen
# @Time:2019/8/309:27
import os
import pickle
from db import models
from conf import settings


# 读取数据
def select(cls,username): # 传的是当前读取文件的类，当前类的对象

    # 获取当前保存文件夹目录
    class_name = cls.__name__
    dir_path = os.path.join(settings.DB_PATH,class_name)

    # 判断文件夹是否存在
    if os.path.isdir(dir_path):
        user_path = os.path.join(dir_path,username)
        # 判断存储对象的文件是否存在
        if os.path.exists(user_path):
            with open(user_path,'rb') as fr:
                self = pickle.load(fr)
                return self









# 保存数据
def save(self): # 传的是当前需要保存的对象self
    # 获取保存文件目录
    class_name = self.__class__.__name__
    dir_path = os.path.join(settings.DB_PATH,class_name)
    # 判断保存文件目录是否存在
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

    # 获取保存对象文件夹
    user_path = os.path.join(dir_path,self.name)
    with open(user_path, 'wb') as fw:
        pickle.dump(self, fw)
        fw.flush()





