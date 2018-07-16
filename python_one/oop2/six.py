class Swan:
    _neck_swan = '天鹅'
    def __init__(self):
        self.age = 2
        print('init',self._neck_swan,self.age)


Swan = Swan()