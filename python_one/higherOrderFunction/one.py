num=abs(-10)
print(num)
#可以将函数本身赋值给变量
x=abs
print(x(-21))

def test(a,b,c):
  return c(a)+c(b)



#把函数作为参数传入，这样的函数称为高阶函数
print(test(-1,-2,abs))


def f(x):
    return x*x


r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))



r2 = map(str,range(1,11))
print(list(r2))



def is_odd(f):
    return f%2==1

r3=filter(is_odd,range(1,11))
print(list(r3))


def do_notEmpty(s):
    return s and s.strip()

r4=filter(do_notEmpty,['a','',None,'B','C'])
print(list(r4))


print(sorted([34,-21,-5,0,11,23]))