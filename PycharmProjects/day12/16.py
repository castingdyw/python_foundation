# 键盘录入一个字符串（要求里面有大写字母、小写字母、数字：如AAAvvv666），
# 去除里面的数字，然后把大写字母变为小写，最终在显示台打印结果.
stri = input('请输入字符串：')
num = ['0','1','2','3','4','5','6','7','8','9']
a = []
for i in stri:
    if i not in num:
        a.append(i)
stri1 = ''.join(a)  # 去除数字
stri2 = stri1.lower()  # 小写
print(stri2)
