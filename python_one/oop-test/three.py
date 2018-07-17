class Money:

    month = [1,2,3]

    def __init__(self):
        print('------------------销售明细--------------------')
        chooseMonth = input('请输入要查询的月份')
        print(chooseMonth)
        if int(chooseMonth) in Money.month:
            print('成功')
        else:
            print('失败')

money = Money()
