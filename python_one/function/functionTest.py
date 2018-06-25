#函数教程

#位置函数
def power(x):
    return x*x


print(power(2))


#位置多个函数
def power(x,y):
    sum = 1
    while y>0:
        y = y-1
        sum = sum +x*x
    return sum


print(pow(2,2))


#---------------------上面的位置函数，必须按照顺序来传递参数---------------------------




#默认函数
def power_def(x,y=2):
    sum = 1
    while y>0:
        y = y -1
        sum = sum*x
    return sum

print(power_def(4))


def school(name,sex,age=6,city='beijing'):
    print(name,sex,age,city)

school('yzc','男',city= 'tianjing')


#---------------------上面的默认函数，传参时可以不指定默认参数---------------------------




#可变参数

#这是一个不可变的
def calc(nums):
    sum = 0
    for num in nums:
        sum = sum+num*num
    return sum


print(calc([1,2,3]))

#可变
def calc_change(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
    return sum

print('calc_change',calc_change(1,2,3))

#将元组作为可变参数，传给方法
nums = (1,2,3)
print('calc_change2',calc_change(*nums))


#关键字参数
def person(name,age,**other):
    print('name:',name,'age:',age,'other:',other)


person('yzc',22,sex='男')
person('yzc',22,job='coding')




info = {'sex:':'男','age:':22}
person('yzc',22,**info)

#命名关键字参数
def person2(name,age,*,sex,job):
    print(name,age,sex,job)

person2('yzc3',22,sex='男',job='coding')

def person3(name,age,*args ,sex,job):
    print(name, age, sex, job)

person3('yzc4', 22, sex='男', job='coding')








