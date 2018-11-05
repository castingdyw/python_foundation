class Person(object):
    n = 0  # 类属性

    def __init__(self):
        Person.n += 1  # 修改类属性

    def eat(self):
        print('能吃')

    def drink(self):
        print('能喝')


zs = Person()
ls = Person()

print('创建了%d个对象' % Person.n)  # 使用类属性


# Person.eat(zs)
