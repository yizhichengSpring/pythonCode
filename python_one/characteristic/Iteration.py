#迭代
for n in range(0,101):
     print(n)


#迭代字典
dicts = {'a':1,'b':2,'c':3,'d':4}

for dict in dicts:
     print(dict)

#上面默认的是迭代key，入过你想迭代value，可以这样做 dicts.value()

for dict in dicts.values():
     print(dict)

#如果你想迭代key,value
for dict in dicts.items():
     print(dict)

#迭代字符串

for str in 'qwerty':
     print(str)



#引入模块
from collections import Iterable


print('字符串能迭代码?',isinstance('asdf', Iterable),type('asdf'))
print('list能迭代码?',isinstance([1,2,3,4], Iterable),type([1,2,3,4]))
print('tuple能迭代码?',isinstance((1,2,3,4), Iterable),type((1,2,3,4)))
print('dict能迭代码?',isinstance({'a':1,'b':2,'c':3}, Iterable),type({'a':1,'b':2,'c':3}))
print('int能迭代码?',isinstance(1234, Iterable),type(1234))



#最大值，最小值
#可选参数
def sort(*nums):

    min = nums[0]
    max = nums[0]

    for num in nums:
        if num < min:
            min = num
        elif num > max:
            max = num
    return (max,min)




nums = sort(11,5,7,9)
print(nums)




