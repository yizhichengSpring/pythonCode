class Geese:
    neck = 'neck'
    wing = 'wing'
    leg = 'leg'
    number = 0

    def __init__(self):
        Geese.number += 1
        print('\n我是第'+str(Geese.number)+'只大雁，我属于雁类，我有以下特征')
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)


#创建4个实例
list = []

for i in range(0,4):
    list.append(Geese())

print(Geese.number)