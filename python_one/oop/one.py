class Student(object):


    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score



    def print_info(self):
        print(self.name,':',self.age,':',self.score)

    # 级别
    def get_grade(self):
        if not isinstance(self.score,(int,float)):
            raise TypeError('score type in (int,float)')
        if self.score >= 90:
            return 'A'
        elif self.score >= 80 and self.score < 90:
            return 'B'
        elif self.score >= 60 and self.score < 80:
            return 'C'
        else:
            return 'D'


bart = Student('yzc',21,91)
lisa = Student('zs',23,23)

print(bart.name,bart.get_grade())
print(lisa.name,lisa.get_grade())
