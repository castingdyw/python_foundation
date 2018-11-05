# def func():
#     global ls
#     print('==1==', ls)
#     ls += [3, 4]
#     print('==2==', ls)
# ls = [1, 2]
# func()
# print('==外==', ls)


# def func(tmp):
#     print('==1==', tmp)
#     tmp += [3, 4]
#     print('==2==', tmp)
#
# ls = [1, 2]
# func(ls)
# print('==外==', ls)

def func(tmp):
    print('==1==', tmp)
    tmp = tmp + [3, 4]
    print('==2==', tmp)

ls = [1, 2]
func(ls)
print('==外==', ls)
