class Swan:
    __neck_name = '天鹅'
    def __init__(self):
        print('__init__()',Swan.__neck_name)



Swan = Swan()
print(Swan._Swan__neck_name)
#print(Swan__neck_name)