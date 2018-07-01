#list

L = ['one','two','three','four']

#下标0开始，0到2，但是不包括3
print(L[0:2])


print(L[:4])


print(L[-2:])


L2 = list(range(0,99))
print(L2)


#取前10
print(L2[:10])
#后10个数
print(L2[-10:])
#11到20
print(L2[10:20])

#前10个数 取偶数
print(L2[:11:2])
#所有数 五个取一个
print(L2[::5])

#tuple
T = (1,2,3,4)
print(T[:3])

#字符串
str = 'abcdefg'
print(str[:3])
print(str[::2])



#去除前后空格
def trim_slice(strContent):
    strLen = len(strContent)
    return strContent[1:strLen-1]


print(trim_slice(' abcde '))