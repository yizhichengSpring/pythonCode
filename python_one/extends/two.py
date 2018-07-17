class Fruit:
    def __init__(self,color= '绿色'):
        Fruit.color = color


    def harvest(self):
        print("水果是"+Fruit.color+"的")



class Apple(Fruit):

    def __init__(self):
        super().__init__()
        print('我是苹果')




apple = Apple()
apple.harvest()