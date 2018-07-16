class TVshow:

    def __init__(self,show):
        self.__show = show


    @property
    def show(self):
        return self.__show



tvshow = TVshow('《战狼2》')
print(tvshow.show)
