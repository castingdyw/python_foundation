#这是我们的第一个程序
#print("hello world")
'''
print("Hello World!")

str1 = "hello"
str2 = "python"
print(str1)
print(str2)

import keyword
print(keyword.kwlist)

i = 0
s = 0
while i <= 100:
    if i % 2 == 0:
        s += i
        i += 1
    else:
        i += 1
print(s)


a = 10
b = 20
c = a if a > b else b
print(c)


i = 0
r = 0
while i <= 100:
    r += i
    print("i = %d" % i)
    i += 2
print("r = %d" % r)
'''
a = 1
while a <= 9:
    b = 1
    while b <= 8:
        print("b = %d" % b,end=" ")
        b += 1
    print("a = %d" % a)
    a += 1