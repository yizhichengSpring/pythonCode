print('hello world')
print('I\'m ok')
print('I\'m ok learning\npython')
print('result true:',True)
print('result false',False)
print('3>2',3>2)
print('2>3',2>3)
print("and",True and True)
print("and",True and False)
print("and",False and False)
print("and", 5>3 and 3>1)
print("or1",True or False)
print("or2",True or True)
print("or3",False or False)
print("not1",not False)
print("not2",not True)
print('not3',not 1>2)
print("none",None)
#age
age = input("your age?")
if int(age)>15 and int(age)<18:
    print("student")
else:
    print("work")
#python 是个动态语言 定义变量的时候，可以不指定类型
name = 'yizhicheng'
print('name',name)
name =21
print('age',name)
x=10
x = x+2
print(x)
a = 100
if a>100:
    print(a)
else:
    print(--a)