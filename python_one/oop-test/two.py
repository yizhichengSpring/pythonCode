class Card(object):

    def __init__(self,no,pwd=123456):
        self.no = no
        if pwd == 123456:
            self.pwd = pwd
        else:
            self.pwd = '重置密码'+str(pwd)

        print(self.no,self.pwd)



card = Card(413026199704054810,134567)