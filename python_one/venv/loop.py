#循环
print(1+2+3)
names = ['小张','小李','小易']
print(names)
for name in names:
    print(name)
#计算1-10的和
nums = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for num in nums:
    sum +=num
print(sum)
#range 生成一个整数序列 再用list() 将其转化为list
money = 0;
nums = list(range(101))
for num in nums:
    money+=num
print(money)
#while循环
sum = 0
num = 99
while num>0:
    sum += num
    num= num-2
print(sum)
#Test
L = ['Bart', 'Lisa', 'Adam']

for name in L:
    print('hello',name,'!')

#打印1-100
num = 1
while num < 100:
    print(num)
    num = num+1
print("end")
#break
num = 1
while num < 100:
    if num >10:
        break
    print(num)
    num = num+1
print("end")
#continue
n = 0
while n <10:
    n = n+1
    if n%2==0:
        continue
    print(n)
