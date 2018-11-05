class Person(object):

    def __new__(cls):
        pass
        # obj = object.__new__(cls)
        # return obj

    def __init__(self):
        self.name = 'zs'

zs = Person()
print(id(zs))

# class Person(object):
#     def __new__(cls, *args, **kwargs):
#         print(args)
#         print(kwargs)
#         obj = object.__new__(cls)
#         return obj
#     def __init__(self, name, sex, age):
#         self.name = name
#
# p = Person('zs', 'man',age = 19)
