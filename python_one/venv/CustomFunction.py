#自定义函数
def my_abs(x):
    #对参数类型进行检查
    if not isinstance(x,(int,float)):
        raise TypeError('我让你传number，你给我传字符串? nmsl?')
    if x>= 0:
        return x
    else:
        return -x

print(my_abs(3))
print(my_abs(-32))

#空函数
def nullFunction():
    pass

import math

def say(name,age):
    print(name,'您今年',age,'岁了')
    return  name,age

#test
def quadratic(a,b,c):
    result=a+b+c
    return  result