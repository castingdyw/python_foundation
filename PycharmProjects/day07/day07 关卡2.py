
# 1. 使用\_\_init\_\_方法，重新实现关卡一练习2里的4、5题，
# 以达到在创建对象的同时，就为对象添加对应的属性的目的
# 2. 为前一题的代码添加\_\_str\_\_方法，以实现当直接打印对象时，能打印出可读性较高的信息

# class People:
#     def __init__(self, company):
#         self.company = company
#         print('公司是%s' % self.company)
#
#     def __str__(self):
#         return '2公司是%s' % self.company
#
# mayun = People('阿里巴巴')
# wanjianlin = People('万达')
# print(mayun)
#
#
# class Car:
#     def move(self):
#         print('汽车在移动')
#         print('颜色%s,型号%s' % (self.color, self.type))
#     def __init__(self, color, type):
#         self.color = color
#         self.type = type
#     def __str__(self):
#         return '2颜色%s, 型号%s' % (self.color, self.type)
#
# BMW_X9 = Car('red', 'A')
# BMW_X9.move()
# print(BMW_X9)

# AUDI_A9 = Car()

# 1. 定义动物类，使用`__init__`方法，在创建对象时接收参数，为其添加name、age、color,food等属性，如“熊猫”，5, “黑白”，“竹子”
# 2. 为动物类定义一个run方法，调用run方法时打印相关信息。如打印出“熊猫正在奔跑”
# 3. 为动物类定义一个eat方法，调用eat方法时打印相关信息。如打印出“熊猫正在吃竹子”
# 4. 通过动物类分别创建出2只不同的动物，分别调用它们的方法，让他们跑起来，吃起来
class Animal:
    def __init__(self, name, age, color, food):
        self.name = name
        self.age = age
        self.color = color
        self.food = food
    def run(self):
        print('%s正在奔跑' % self.name)
    def eat(self):
        print('%s正在吃%s' % (self.name, self.food))

dog = Animal('xiaohei', 12, 'red', 'cake')
dog.run()
dog.eat()
# cat = Animal()类似





