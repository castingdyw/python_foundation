#主要看内存地址变化没，可变类型，不可变类型
#显示data是100，函数调用后a也是100，a后来赋值200，是不可变类型，现在就是data是100，a是200
# def test1(a):
#     a = 200
#     print('test1--- %d' % a)
# data = 100  # data 是一个数字
# test1(data)
# print('main --- %d' % data)


#列表是可变类型，data是[11],a是[11]，a.append(22),内存地址不变，data和a一样
# def test1(a):
#     a.append(22)
#     print('test1--- %s' % a)
# data = [11]  # data 是一个列表
# test1(data)
# print('main --- %s' % data)

#开始data是[11]，a是[11]，后来a赋值[],内存地址变了，data没变，a是[22]
def test1(a):
    a = []
    a.append(22)
    print('test1--- %s' % a)
data = [11]  # data 是一个列表
test1(data)
print('main --- %s' % data)

#函数内修改i全局变量
# def test1(a):
#     global data
#     data = [22]
#     print('test1--- %s' % data)
# data = [11]  # data 是一个列表
# test1(data)
# print('main --- %s' % data)