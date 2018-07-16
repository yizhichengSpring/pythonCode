class TVshow:
    list_film = ['战狼2','红海行动','熊出没','喜洋洋']

    def __init__(self,show):
        self.__show = show


    @property
    def show(self):
        return self.__show


    @show.setter
    def show(self,value):
        if value in TVshow.list_film:
            self.__show = '您选择了《'+value+"'》，稍后请播放"
        else:
            self.__show = '电影院不支持该影片'



tvShow =TVshow('战狼2')
print(tvShow.show)
print('您可以选择一部',tvShow.list_film)
tvShow.show = '红1海行动'
print(tvShow.show)
