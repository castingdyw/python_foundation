#求1-5的阶乘
#开始先把5-2的放在那里，得到1后，由此倒推，求2，3，4，5
def jc(n):
    if n != 1:
        res = n * jc(n-1)
    else:
        res = 1
    return res
print(jc(5))


