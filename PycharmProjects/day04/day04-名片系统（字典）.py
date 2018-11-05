#信息有姓名，电话，地址

# 建存放数据空列表
cards = []

while True:
    #打印信息
    print('=======================')
    print('欢迎使用 名片管理系统 v1.0')
    print('1.添加名片')
    print('2.删除名片')
    print('3.修改名片')
    print('4.查看名片')
    print('5.查看所有名字')
    print('0.退出系统')
    print('=======================')

    #获取数据
    com = input('请输入指令：')
    #添加名片
    if com == '1':
        info = {}
        name = input('请输入名字：')
        tel =  input('请输入电话：')
        addr = input('请输入地址：')
        info['name'] = name
        info['tel'] = tel
        info['addr'] = addr
        cards.append(info)

    #删除名片
    elif com == '2':
        name_del = input('请输入要删除的名字：')
        for card_del in cards:
            if name_del == card_del['name']:
                cards.remove(card_del)
                print('%s的名片已删除' % name_del)
                break
        else:
            print('没有这个名字，无法删除')

    #修改名片
    elif com == '3':
        name_old = input('请输入要修改的名字：')
        name_new = input('请输入修改后的名字：')
        for card_gai in cards:
            if name_old in card_gai['name']:
                card_gai['name'] = name_new
                break
        else:
            print('没有这个名字，无法修改')

    #查看名片
    elif com =='4':
        name_find = input('请输入要查看的姓名：')
        for card_find in cards:
            if name_find == card_find['name']:
                print('姓名：%s  电话：%s  地址：%s' % (card_find['name'], card_find['tel'], card_find['addr']))
                break
        else:
            print('没有这个名字')

    #查看所有名片
    elif com == '5':
        for card_find in cards:
            print('姓名：%s  电话：%s  地址：%s' % (card_find['name'], card_find['tel'], card_find['addr']))

    #退出系统
    elif com == '0':
        break

    #输入不正确
    else:
        print('输入无法识别，请重新输入')

print('程序结束')

