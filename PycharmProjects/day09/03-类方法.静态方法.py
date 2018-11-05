class Person(object):
    __n = 0  # 类属性

    def __init__(self):
        Person.__n += 1  # 修改类属性

    def eat(self):
        print('能吃')

    def drink(self):
        print('能喝')

    @classmethod
    def get_n(cls):
        return '数字Person.__n:%d' % cls.__n

    @staticmethod
    def add(a, b):
        return a + b

zs = Person()
print(Person.get_n())

sum = Person.add(1,2)
print(sum)