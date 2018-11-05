# tmp = {'name':'zs','age':18,'sex':'男'}
# for i in tmp.keys():
#     print(i)
# for i in tmp.values():
#     print(i)
# for i in tmp.items():
#     print(i)
# for k,v in tmp.items():
#     print(k,v)

# info = {}
# name = input('姓名：')
# age = input('年龄：')
# sex = input('性别：')
# info['name'] = name
# info['sge'] = age
# info['sex'] = sex
# print(info)


# 查看笔记本键盘1-9还有0号键其上方的字符，要求用户输入"1"，那么输出"!",输入"2"，那么输出"@",以此类推
# 用字典完成这个任务
# 用户如果输入的字符长度超过1或者是除数字以外其他字符，提示"未收录该字符的含义，请重新输入"
a = {'1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'('}

while True:
    b = input('请输入数字：')
    if len(b) >= 2:
        print('未收录该字符的含义，请重新输入')
        continue
    else:
        print(a[b])
        break