# 请写出一个Car作为基类,BMW类继承于Car类,基类中有__init__方法(包含name,color)和run方法.
class Car(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print('名字%s, 颜色%s' % (self.name, self.color))
    def run(self):
        pass

class BMW(Car):
    def __init__(self, name, color, age):
        self.age = age
        super(BMW, self).__init__(name, color)

bmw= BMW('A', 'red', 10)


# 写出一个简单的多继承案例，并使用子类对象调用所有的父类方法。比如 LuoZi 类同时继承 Ma类、Lv类
class Ma(object):
    def run(self):
        print('马跑得快')
    def zou(self):
        print('嘛也能走')

class Lv(object):
    def zou(self):
        print('驴走的远')

class LuoZi(Ma, Lv):  # 多继承
    pass

luozi = LuoZi()
luozi.run()
luozi.zou()
Ma.zou(luozi)  # 父类方法同名，强制调用
print(LuoZi.__mro__)

print('===============================================')
# 下面有一个类,请创建一个子类并重写类中的方法
# 修改上一题的代码，在子类方法里，使用三种不同方式调用父类的方法
# 	```python
# 	class Car(object):
# 		def run(self):
# 			print("奔驰在路上!")
class Car(object):
    def run(self):
        print("奔驰在路上!")

class BMW(Car):
    def run(self):
        print('子类重写父类')
        # super().run()
        super(BMW, bmw).run()

bmw = BMW()
bmw.run()
# bmw.run()
# Car.run(bmw)
# super(BMW,bmw).run()
# super().run()


