#获取文件名

#打开文件

#读取数据

#写入数据

#关闭文件


# def test():
#     '''测试函数'''
#     print('a')
# test()


def jc(n):
    if n != 1:
        s = n * jc(n-1)
    else:
        s = 1
    return s

a = jc(5)
print(a)


def suan(a,b,c):
    res = c(a,b)
    return res

s = lambda x,y:x+y

rr = suan(1,2,s)
print(rr)