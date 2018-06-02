#集合学习
classMates = ['小李','小红','小张']
print(classMates[0])
print(classMates[1])
print(classMates[2])
#查看集合
print(classMates)
#在集合最后面追加一个元素
classMates.append("小易")
print(classMates)
#在该下标，新增一个元素
classMates.insert(0,'小白')
print(classMates)
#删除该下标下的元素
classMates.pop(0);
print(classMates)
#替换
classMates[0] = 'xiaoli'
print(classMates)
#集合任意类型都可以
yzc = ['yizhicheng',21,True]
print('易志成的个人简介',yzc)
#list 嵌套list
school = ['oneClass',['小王啊','小孙啊','小爱啊']]
print(school)
#三个集合 分开表示
phone = ['iphone','xiaomi','huawei']
computer = ['macbook pro','lenovo','dell']
langeage = ['python','java','unix']
shop = [phone,computer,langeage]
print(shop)
#取值 一维数组取值
print('一维',computer[0])
#取值 二维数组取值
print('二维',shop[1][0])
#空集合
twoClass = []
print(len(twoClass))



##########################################
#tuple 一旦定义 不能修改 安全啊
threeClass = ('周杰伦','林俊杰')
print(threeClass)
print(threeClass[1])
#陷阱
t = (1,2)
print(t)
t = ()
print(t)
t = (1)
print("有没有想过为什么只有一个元素，它就不是tuple了，()都没有输出啊",t)
#因为 只有一个(元素) 的时候,python怎么知道你是集合还是小括号呢?
#然后python规定，只有一个元素，按照，小括号计算
#但是也有解决的方法啦 加个,就可以了
t1 = (1,)
print(t1)
#测试
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
#打印apple
print('打印',L[0][0])
#打印pyhton
print('打印',L[1][1])
#打印Lisa
print('打印',L[2][2])

