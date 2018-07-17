age = 2
if age >=18:
    print('大学生')
else:
    print("高中生")

#eiif 相当于 else if
# studentAge = input('your age?')
# if int(studentAge)<12:
#     print("小学生")
# elif int(studentAge)>12 and int(studentAge) <15:
#     print("初中生")
# else:
#     print("高中生")

#oop-test
height = 1.75
weight = 80.5

bmi = weight / (height*height)
bmi = int(bmi);
print(bmi)
if bmi <18.5:
    print('过轻')
elif bmi >18.5 and bmi <25:
    print('正常')
elif bmi >25 and bmi < 28:
    print('过重')
elif bmi > 28 and bmi <32:
    print('肥胖')
elif bmi >32:
    print('严重肥胖')



