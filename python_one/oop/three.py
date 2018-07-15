class Student(object):

    def __init__(self,name,age):
        self.__name = name
        self.__age = age



    def print_info(self):
        print(self.__name,':',self.__age)


    def get_name(self):
        return self.__name


    def get_age(self):
        return self.__age


    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age






zhangsan=Student('zs',25)
print(zhangsan.get_name(),zhangsan.get_age())
zhangsan.set_name('zs2')
print(zhangsan.get_name())