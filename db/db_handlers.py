# Author:xichen
# @Time:2019/9/214:49

import os
import pickle
from conf import settings

def save(self):
    class_name = self.__class__.__name__
    dir_path = os.path.join(settings.DB_PATH,class_name)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
        
    user_path = os.path.join(dir_path,self.name)
    with open(user_path,'wb') as fw:
        pickle.dump(self,fw)
        fw.flush()



def select(cls,name):
    class_name = cls.__name__
    dir_path = os.path.join(settings.DB_PATH, class_name)
    if os.path.isdir(dir_path):
        user_path = os.path.join(dir_path,name)
        if os.path.exists(user_path):
            with open(user_path,'rb') as fr:
                self = pickle.load(fr)
                return self
                
        


