# def ass(a,b,cc):
#     res = cc(3,b)
#     print(res)
#
# s = lambda x,y:x+y
# ass(1,2,s)

# 使用匿名函数，实现调用一个函数处理加减乘除。(不需要考虑被除数为 0 的情况。)
# def suan(a,b,cc):
#     r = cc(a,b)
#     print(r)
#
# jia = lambda x,y:x+y
# jian = lambda x,y:x-y
# cheng = lambda x,y:x*y
# chu = lambda x,y:x/y
#
# suan(2,5,jian)


# s = lambda x,y:x+y
# res = s(2,5)
# print(res)



# 使用匿名函数为下面的列表排序
# * a = [{'name':'zhangsan','age':18},{'name':'lisi','age':19},{'name':'wanger','age':16}]
# * 按照姓名排序并打印
# * 按照年龄排序并打印
a = [{'name':'zhangsan','age':18},{'name':'lisi','age':19},{'name':'wanger','age':16}]
s = lambda x:x['name']
a.sort(key = s)
print(a)