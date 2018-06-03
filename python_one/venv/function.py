#绝对值
print(abs(100))
print(abs(-100))
#返回最大的值
age = [1,2,6,4,5]
print(max(age))
#数据类型转换
print(int(123))
print(int(123.23))
print(str(1.23))
#把函数赋值给一个变量
a=abs
print(a(-6))
#把一个整数换成16进制表示的字符串
print(hex(255))
print(hex(1000))
#调用自定义函数
from CustomFunction import my_abs
from CustomFunction import  say
from CustomFunction import  quadratic
from CustomFunction import *
import CustomFunction
print(my_abs(-31))
print(my_abs(123))
name  =say('易志成',22)
print(name)
result = quadratic(4,2,3)
print(result)
