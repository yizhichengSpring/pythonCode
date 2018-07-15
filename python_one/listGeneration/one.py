# #列表生成式
# print(list(range(1,10)))
#
# #1*1 2*2 3*3 的值
# def cale():
#     L = []
#     for num in range(1, 11):
#         L.append(num * num)
#     return L
#
#
#
# print(cale())
#
#
#
# #1*1 2*2 3*3 列表生成式的写法
# nums = [ n*n for n in range(1,11)]
# print(nums)
#
#
# #先写一个空列表 [] 然后跟上你的循环体 列表生成式 就写完了
# nums2 = [i*i for i in range(1,11)]
# print(nums2)
#
#
# #计算10以内的偶数平方,并一一列举出来
# nums3 = [j*j for j in range(1,11) if j%2==0]
# print(nums3)
#
#
# #全排列 谁这样写啊平时
# str = [m+n for m in 'abc' for n in 'def']
# print(str)
#
#
#
# #导入os模块
# import os
#
# dir=[d for d in os.listdir('.')]
# print(dir)
#
#
#
# #打印dict值
# strNum = {1:'a',2:'b',3:'c',4:'d'}
#
# for m,n in strNum.items():
#     print(m,n)

#列表生成式写法
# strNum = {1:'a',2:'b',3:'c',4:'d'}
#
#
# result =[str(k)+'='+m for k,m in strNum.items()]
# print(result)
#
#
#
# upplower = ['A','B','C','D']
#
# print([h.lower() for h in upplower])


#Test
# L = ['Hello', 'World', 18, 'Apple', None]
# print([i.lower() for i in L if isinstance(i,str) == True])


