class Movie:
    movie_list = ['红海行动','战狼2','喜羊羊','熊出没']

    def __init__(self,movie):
        self.__movie = movie


    @property
    def show(self):
        return self.__movie


    @show.setter
    def set_movie(self,moviler):
        if moviler in self.movie_list:
            self.__movie = '您好，您选择的影片《'+moviler+'》即将播放'
        else:
            self.__movie = '您选择的电影《'+moviler+'》不存在'



movie = Movie('战狼I')
print(movie.show)

movie.set_movie = '战狼22'
print(movie.show)