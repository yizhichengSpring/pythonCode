#python函数学习 卧槽，今天的心情是真的糟糕

#abs 返回绝对值
print(abs(10))

print(abs(-5))

print(abs(-12.88))


#max可以传入多个参数 返回最大值
print(max(1,2,3,45))

print(min(-1,2,3,-3))


#数据类型切换

#int
print(int('1'))
print(int('23'))

#float
print(float('2.35'))
print(float(3))

#str
print(str('1.23'))
print(str('3.1415926'))

#bool 非0都是True
print(bool(1))
print(bool(0))
print(bool(-2))


#自定义函数
def myabs(x):
    if x>0:
        return x
    else:
        return -x


print(myabs(-3))

#pass作为占位符
def myabs2(x):
    pass

#类型检查 isinstance 是否包含其中类型
def myabs_strong(x):
    if not isinstance(x,(int,float)):
        raise  TypeError('not int or float')
    else:
        myabs(x)


myabs_strong(2)
