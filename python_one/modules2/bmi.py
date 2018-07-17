def fun_bmi(person,height,weight):
    '''
    功能:根据身高和体重计算bmi指数
    :param person:
    :param height:
    :param weight:
    :return:
    '''

    print(person+"的身高"+str(height)+"米\t体重:"+str(weight)+"千克")
    bmi = weight/(height*height)
    print(person+"的BMI指数为"+str(bmi))




# fun_bmi('yzc',1.86,90)