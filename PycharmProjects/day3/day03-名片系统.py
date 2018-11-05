#打印信息--获取信息--判断
#添加名片--查看名片--其它随便

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
name_all = []
while True:
    #获取信息
    num = input('请输入数字：')

    #添加名片
    if num == '1':
        name = input('输入添加的名字：')
        name_all.append(name)

    #删除名片
    elif num == '2':
        name_del = input('输入要删除的名字：')
        if name_del in name_all:
            name_all.remove(name_del)
        else:
            print('没有这个名字，无法删除')

    #修改名片
    elif num == '3':
        name_old = input('输入要修改的名字：')
        name_new = input('输入修改后的名字：')
        if name_old in name_all:
            name_index = name_all.index(name_old)
            name_all[name_index] = name_new
        else:
            print('没有这个名字')

    #查看名片
    elif num == '4':
        name_find = input('输入查看的名字：')
        if name_find in name_all:
            print('有名字')
        else:
            print('没有名字')

    #查看所有名字
    elif num == '5':
        for i in name_all:
            print(i)

    #退出系统
    elif num == '0':
        break

    else:
        print('你的输入有误，请重新输入')

print('程序结束')

