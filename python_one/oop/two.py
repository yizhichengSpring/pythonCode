class Teacher(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age



    def printInfo(self):
        print(self.name,':',self.age)






zhang = Teacher('zhangsan',29)
zhang.printInfo()

