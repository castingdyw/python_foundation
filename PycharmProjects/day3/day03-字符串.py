
# 设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
# 打印出字符串长度
# 使用切片逆序打印出字符串
# while True:
#     a = input('输入：')
#     if len(a) < 31:
#         print(len(a))
#         print(a[::-1])
#         break
#     else:
#         print('请重新输入')


# 编写代码模拟用户登陆。要求：用户名为 python，密码 123456，
# 如果输入正确，打印“欢迎光临”，程序结束，如果输入错误，提示用户输入错误并重新输入。
# account = 'python'
# password = '123456'
#
# while True:
#     b = input('用户名：')
#     c = input('密码：')
#     if b == account and c == password:
#         print('wlcome')
#         break
#     else:
#         print('again')


# 要求从键盘输入用户名和密码
# 校验格式是否符合规则，用户名长度6-20，并且用户名必须以字母开头
# 如果不符合，打印出不符合的原因，并再次提示输入
# while True:
#     a = input('用户名：')
#     b = input('密码：')
#
#     if (6 <= len(a) <= 20) and (a[0].isalpha()):
#         print('success')
#         break
#     else:
#         print('again')


# 使用个三个变量来记录用户输入的信息，包含姓名、电话、性别
# 姓名长度不是在6-20范围内，则提示错误
# 电话号码长度不是11，则提示错误
# 性别不是男或女，则提示错误
# 所有信息校验通过后，打印名片信息，程序结束
a = input('姓名：')
b = input('电话：')
c = input('性别：')

# if len(a) >= 20 or len(a) <= 6:
#     print('a错误')
# elif len(b) != 11:
#     print('berror')
# elif c != '男' and c != '女':
#     print('cerror')
# else:
#     print(a,b,c)

if len(a) >= 20 or len(a) <= 6:
    print('姓名错误')
if len(b) != 11:
    print('号码error')
if c != '男' and c != '女':
    print('性别error')
if 6 <= len(a) <= 20:
    if len(b) == 11:
        if c == '男' or c == '女':
            print(a,b,c)










