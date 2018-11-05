# 1. 创建一个动物类,并通过__init__方法接受参数(name),使用私有属性name保存参数值，并打印"init被调用".
# 2. 修改上一题的代码，提供可以重新设置私有属性__name的方法，限制条件为字符串长度小于10,才可以修改。并提供方法可以获取私有属性 __name 的值。
# 3. 使用动物类，实例化一个spider对象取名"蜘蛛侠".
# 4. 尝试调用方法修改蜘蛛侠的名字为"你嘴巴不停的好邻居蜘蛛侠",并打印验证是否修改成功
# 5. 尝试调用方法修改蜘蛛侠的名字为"你的好邻居蜘蛛侠",并打印验证是否修改成功
class Animal:
    def __init__(self, name):
        self.__name = name
        print('init被调用')
    def set_name(self, new_name):
        if len(new_name) < 10:
            self.__name = new_name
        else:
            print('不能修改%s' % self.__name)
    def get_name(self):
        return self.__name

spider = Animal('蜘蛛侠')
spider.set_name('你嘴巴不停的好邻居蜘蛛侠')
print(spider.get_name())
spider.set_name('你的好邻居蜘蛛侠')
print(spider.get_name())

# 利用继承编写下面一段代码
# **要求：**
# 1. 动物:吃,喝,跑,玩
# 2. 猫:喵喵叫
# 3. 狗:旺旺叫
# 4. 猫、狗继承于动物,并且有2、3中自己的方法.
# 5. 创建猫和狗的对象，并调用可用的所有方法
class Animal:
    def eat(self):
        print('动物能吃')
    def drink(self):
        print('动物能喝')
    def run(self):
        print('动物能跑')
    def play(self):
        print('动物能玩')
class Cat(Animal):
    def miao(self):
        print('猫能喵喵叫')
class Dog(Animal):
    def wang(self):
        print('狗能汪汪叫')
cat = Cat()
cat.miao()
cat.eat()

# 1. 定义一个人的基类,类中要有初始化方法,方法中初始化人的姓名,年龄.
# 2. 提供__str__方法，返回姓名和年龄信息
# 2. 将类中的姓名和年龄私有化.
# 3. 提供获取私有属性的方法.
# 4. 提供可以设置私有属性的方法.
# 5. 设置年龄时限制范围(0-100).
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __str__(self):
        return '姓名%s, 年龄%s' % (self.__name, self.__age)
    def set_info(self, new_name, new_age):
        self.__name = new_name
        if 0 <= new_age <= 100:
            self.__age = new_age
        else:
            print('%d 不能被修改' % self.__age)
    def get_info(self):
        return '姓名%s, 年龄%s' % (self.__name, self.__age)

person = Person('ding', 18)
print(person)
person.set_info('ls', 56)
print(person.get_info())

# 1. 创建一个动物的基类,其中有一个run方法
# 2. 创建一个Cat类继承于动物类
# 3. 创建一个Dog类继承于动物类
# 4. Cat类中不仅有run方法还有eat方法
# 5. Dog类中方法同上
# 6. 创建一个Human类，提供letRun函数，可以接收动物及其子类对象，并调用run方法
# 7. 编写测试代码以验证功能正常
class Animal:
    def run(self):
        print('动物能跑')
class Cat(Animal):
    def eat(self):
        print('猫能吃')
class Dog(Animal):
    def eat(self):
        print('狗能吃')
class Human:
    def letRun(self):
        # self.item = item
        # self.item.run()
        animal.run()
        # self.item.eat()

print('==================')
animal = Animal()
human = Human()
human.letRun()






