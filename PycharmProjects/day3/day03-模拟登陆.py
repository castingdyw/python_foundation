#获取账号密码
a = input('请输入账号：')
b = input('请输入密码：')

#验证是否正确
account = 'dyw'
password = '123'

if (a == account) and (b == password):
    print('登陆成功')
else:
    print('登陆失败')