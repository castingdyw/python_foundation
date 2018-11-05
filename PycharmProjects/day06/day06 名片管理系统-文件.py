# print("---------------------------")
# print("      名片管理系统 V1.0")
# print(" 1:添加名片")
# print(" 2:删除名片")
# print(" 3:修改名片")
# print(" 4:查询名片")
# print(" 5:显示所有名片")
# print(" 6:保存数据")
# print(" 7:退出系统")
# print("---------------------------")

def add_card():
    info = {}
    name = input('请输入姓名：')
    tel = input('请输入电话：')
    addr = input('请输入地址：')
    info['name'] = name
    info['tel'] = tel
    info['addr'] = addr
    cards.append(info)

def del_card():
    del_name = input('请输入要删除的名字：')
    for del_card in cards:
        if del_name == del_card['name']:
            cards.remove(del_card)
            print('您要删除的信息已经删除')
            break
    else:
        print('没有这个名字，无法删除')

def mod_card():
    mod_name = input('请输入要修改的名字：')
    for mod_cards in cards:
        if mod_name == mod_cards['name']:
            new_name = input('请输入新名字：')
            mod_cards['name'] = new_name
            print('您要修改的名字已经修改')
            break
    else:
        print('没有这个名字，无法修改')

def find_card():
    find_name = input('请输入要查询的名字：')
    for find_cards in cards:
        if find_name == find_cards['name']:
            print('姓名：%s 电话：%s 地址：%s' % (find_cards['name'], find_cards['tel'], find_cards['addr']))
            break
    else:
        print('没有找到这个名字')

def apper_card():
    for eve_card in cards:
        print('姓名：%s 电话：%s 地址：%s' % (eve_card['name'],eve_card['tel'],eve_card['addr']))

def save_card():
    f = open('card.txt','w')
    for i in cards:
        f.write('姓名：%s 电话：%s 地址：%s' % (i['name'], i['tel'], i['addr']))
        f.write('\n')
    f.close()

def main():
    while True:
        # 打印提示
        print("---------------------------")
        print("      名片管理系统 V1.0")
        print(" 1:添加名片")
        print(" 2:删除名片")
        print(" 3:修改名片")
        print(" 4:查询名片")
        print(" 5:显示所有名片")
        print(" 6:保存数据")
        print(" 7:退出系统")
        print("---------------------------")

        #获取命令
        command = input('请输入指令：')

        # 添加名片
        if command == '1':
            add_card()


        # 删除名片
        if command == '2':
            del_card()

        # 修改名片
        if command == '3':
            mod_card()

        # 查询名片
        if command == '4':
            find_card()

        # 显示所有名片
        if command == '5':
            apper_card()

        # 保存数据
        if command == '6':
            save_card()

        # 退出系统
        if command == '0':
            yn = input('您确定退出系统：y/n')
            if yn == 'y':
                break
            else:
                continue

cards = []
main()
print('程序结束')