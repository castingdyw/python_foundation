# def add(*args):
#     s = 0
#     for i in args:
#         s += i
#     print(s)
#
# ls = [1, 2, 3, 4, 5]
#
# add(*ls)

# def func(a, b, *args, **kwargs):
#     print(a)
#     print(b)
#     print(args)
#     print(kwargs)
#
# func(3, 8, 4, 6, 1, m=3, n=4)


def func(a, b, c=100):
    print(a, b, c)

func(3,6)