class Person:
    def run(self):
        self.__myprint('快跑')
        print('人可以跑')

    def eat(self):
        print('人可以吃')

    def __myprint(self, content):
        print('person说：', content)

p = Person()
# p.run()
# p.__myprint__()  私有方法不能在类的外部调用
p.run()



class Person(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __str__(self):
        return '名字%s, 年龄%s' % (self.__name, self.__age)
    def __run(self):
        print('人可以跑')
    def get_run(self):  # 通过公有方法访问私有方法
        self.__run()

p = Person('ding', 18)
print(p)
# p.run()
p.get_run()