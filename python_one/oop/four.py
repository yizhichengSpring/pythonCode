class Student(object):

    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender



    def get_Gender(self):
        return self.__gender


    def set_Gender(self,gender):
        if gender=='男' or gender == '女':
            self.__gender = gender
        else:
            raise ValueError('gender mustbe 男 or 女')


    def print_info(self):
        print(self.__name,':',self.__age,':',self.__gender)




zhangsan = Student('zhangsan',22,'男')
zhangsan.set_Gender('红艺人')
zhangsan.print_info()