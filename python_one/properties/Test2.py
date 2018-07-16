class Test:

    list_film = ['战狼2','红海行动','熊出没','喜羊羊']

    def __init__(self,show):
        self.__show = show


    @property
    def show(self):
        return self.__show


    @show.setter
    def show(self,movie):
        if movie in Test.list_film:
            print('您选择的是',movie,'即将播放')
        else:
            print('不好意思，本影院暂不提供该影片')


test = Test('战狼22')
print(test.show)
print(test.list_film)
test.show = '红海行动2'

