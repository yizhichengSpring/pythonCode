# #自定义函数 计算阶乘
# def power(x,y):
#     s = 1
#     while(y>0):
#         y = y-1
#         s=s*x
#     return s
#
#
# def power2(x,y=2):
#     s = 1
#     while(y>0):
#         y = y-1
#         s=s*x
#     return s
#
#
# #调用
# num = power(3,2)
# print(num)
#
# #调用默认参数
# num2 = power2(2)
# print(num2)
#
#
#
#
# #school
# def school(name,sex,age=6,city='北京'):
#     print(name,sex,age,city)
#
#
#
# #调用
# school('yzc','男')
# school('yzc2','女',7,city='上海')
#
#
#
# #计算 不可变参数
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum+n*n
#     return sum
#
#
#
# #测试
# print(calc((1,2,3)))
#
#
#
# #可变参数 加*即可
# def calcStrong(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum+n*n
#     return sum
#
#
# print(calcStrong(3,3,3))
#
#
# #关键字参数
#
# def person(name,age,**param):
#     print('name:',name,'age:',age,'job:','other',param)
#
#
# #调用
# person('yzc',22,work='coding')
# person('yzc',22,sex='男')
#
#
#
# params = {'country':'China','home':'河南'}
#
# person('yzc',22,**params)

#命名关键字
def persion_name(name,age,*,city,job):
    print(name,age,city,job)

persion_name('yzc',22,city='beijing',job='coding')



def persion_name2(name,age,*,city='beijing',job):
    print(name,age,city,job)



persion_name2('yzc',22,job='coding')
