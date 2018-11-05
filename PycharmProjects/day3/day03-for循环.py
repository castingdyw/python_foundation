for i in 'python':
    if i == 'm':
        break
    print(i)
else:
    print('循环正常结束')
print('程序结束')


foo = list(range(0, 10))*2
print(foo)
for i in foo[:]:
    if (i % 3 == 0) or (i % 2 == 0):
    # if i % 3 == 0:
        foo.remove(i)

print(foo)