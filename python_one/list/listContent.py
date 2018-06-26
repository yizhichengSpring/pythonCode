# # # # #最快的方法打印一段区间数
# # # # print(list(range(1,11)))
# # # #
# # # # L = []
# # # #
# # # # for num in range(1,11):
# # # #     L.append(num*num)
# # # #
# # # #
# # # # print(L)
# # # #
# # # # #列表生成器
# # # # print([x*x  for x in range(1,11)])
# # # #输出1-10 之内的奇数
# # # print([x for x in range(1,11) if x%2!=0])
# # #
# # # import os
# # #
# # # #列出当前目录所有文件
# # # print([dir for dir in os.listdir('.')])
# # #
# # #
# # # #for 遍历多个文件
# # # dicts = {'a':1,'b':2,'c':3,'d':4}
# # #
# # # print(dict for dict in dicts.items())
# # #
# # #
# # # for dict in dicts.items():
# # #     print(dict)
# #
# #
# # a = abs(-10)
# # print(a)
# #
# # b=abs
# # print(b(-2))
# #
# #
# # def num(a,b,c,):
# #     return c(a)+c(b)
# #
# #
# #
# # print(num(-1,-2,abs))
# #
# #
# #
# #
#
#
# def math(x):
#     return x*x
#
#
# L=map(math,list(range(1,11)))
# print(list(L))

# print(list(map(str,range(1,11))))