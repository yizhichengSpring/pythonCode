class Rate:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width*self.height



Rate = Rate(800,600)
print('面积为',Rate.area)
