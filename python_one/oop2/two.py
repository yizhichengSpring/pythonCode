class Geese2:
    def __init__(self,beak,wing,claw):
        print('我是大雁')
        print(beak)
        print(wing)
        print(claw)

    def fly(self,state='沙发'):
        print(state)




beak = '我是头部'
wing = '翅膀'
claw = '爪子'
Geese2 = Geese2(beak,wing,claw)
Geese2.fly()