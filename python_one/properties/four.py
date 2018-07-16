class TVshow:

    def __init__(self,show):
        self.__show = show


    @property
    def show(self):
        return self.__show




tvShow = TVshow('战狼1')
print(tvShow.show)

