# # num = 1.12645
# # print(num)
# # # 保留小数位数 支持四舍五入
# # result = round(num,2)
# # print(result)
#
#
#
#
#
# #计算两个数字相加的和
# def add(x,y):
#     result = x+y
#     return  result
#
#
# def print_code(code):
#     print(code)
#
#
#
#
# result = add(1,2)
# str = print_code('python')
# print(result,str)
#
#
#
# #return 多个返回值
# def math(param1,param2):
#     one = param1*3+1
#     two = param2*10+2
#     return one,two
#
#
#
# print(type(math(1,2)))
# return1,return2 = math(1,2)
# print(return1,return2)
#
#
#
#
#
# #序列解包
# d = 1,2,3
# a,b,c = d
# print('序列解包',a,b,c)
#
#
#
#
# #自定义函数
# def print_student_info(name,age='22',sex='男',school = '上海交通大学'):
#     print('我是'+name)
#     print(type(age))
#     print('我'+age+'岁')
#     print('我是'+sex+'生')
#     print('我在'+school+'上学')
#
#
# print_student_info('yzc')
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print_student_info('易志成')
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print_student_info('spring2018','23','女')
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# print_student_info('kiff',sex='半兽',school='召唤师峡谷学校')





#计算器
def nums(num1,num2=2,num3=3):
    result = num1+num2+num3
    return result,num1,num2,num3



result,num1,num2,num3=nums(1,num3=9)
print(result,num1,num2,num3)