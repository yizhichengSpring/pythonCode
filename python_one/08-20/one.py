# print('猜一个数字?')
# number = int(input('请输入给出的数字?'))
# print(number%3,number%5,number%7,type(number%3))
# if number%3 ==2 and number%5 ==3 and number%7 ==2:
#     print(number,'符合条件')
# else:
#     print('不符合条件!!!')

# print('请勿酒后开车!!!')
# proof = int(input("请输入每100Ml中酒精含量:"))
# if proof < 20:
#     print('您还未构成酒后驾驶')
# else:
#     if  80 >proof >=20:
#         print('酒后标准')
#     else:
#         print('醉驾')

# a = 10
# b = 6
# r = a if a>b else b
# print(r)



# print('c猜数字！！')
# none = True
# number = 0
# while none:
#     number += 1
#     if number%3 ==2 and number%5 ==3 and number%7 ==2:
#         print('数字正确',number)
#         none = False


#计算0-100的相加
# result = 0
# for i in range(101):
#     result += i
# print(result)


# for i in range(0,10,2):
#     print(i,end= ' ')




# print('求数字')
#
# for n in range(0,1000):
#     if n % 3 == 2 and n % 5 == 3 and n % 7 == 2:
#         print(n,end=' ')



#九九乘法表


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(i)+"x"+str(j)+"="+str(i*j)+"\t",end= '')
#     print(' ')


total = 0
for i in range(1,100):
    if i %7 == 0:
        total += 1
        continue
    else:
        if str(i).endswith('7'):
            total += 1
            continue
print('一共',total,'次')