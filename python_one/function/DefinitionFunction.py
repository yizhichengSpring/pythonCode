#计算一元二次方程的两个解 ax2 + bx + c = 0

import math

def quadratic(a,b,c):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float))):
        raise TypeError('type error yzc say .....')
    L = []
    for x in range(0,100):
        if a*x*x+b*x+c == 0:
            L.append(x)
    return L





# L = quadratic(1,3,'WEQRT')
# print(L)


# 1*1+3*1+-4



def power(x,n=2):
    if not (isinstance(x,(int,float)) and isinstance(n,(int,float))):
        raise TypeError('x,n must be int or float')
    result = 1
    while n >0:
        n = n-1
        result = result*x
    return result


#
# print(power(5,3))


#默认函数
def student_info(name,gender,age=6,city='beijing'):
    if not isinstance(age,(int)):
        raise TypeError('age must type of int')
    print('name:',name,'gender:',gender,'age:',age,'city:',city)


# student_info('yzc','男',age=22)



#可变函数
#计算 a*a+b*b+c*c
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
    return sum


# #赋值时可以写多个，甚至不写
# print(calc(1,3,5,7))
# print('无',calc())



#关键字参数
def person(name,age,**others):
    if not isinstance(age,(int)):
        raise TypeError('age type must be type of int')
    print('name:',name,'age:',age,'others:',others)


yizc = {'city':'beijing','job':'beijing','gender':'男'}
person('yzc',22,**yizc)






