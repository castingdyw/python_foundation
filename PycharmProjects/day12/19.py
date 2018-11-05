# 定义一个汽车类（Car）：
#          有2个实例属性：
# 1名字，2损耗（loss）（价格，油耗，公里数）（3个值放在列表中）
# 有以下实例方法：
# 1：获取汽车姓名：getName();
# 2：获取汽车价格：getPrice();（从列表中获取）
# 3：获取汽车的损耗值：getLoss()；（油耗乘以公里数）
# 定义两个汽车对象，调用上述方法，比较二者的价格及损耗值，并打印结果
# 比如：
# Bmw = Car（”宝马”，[60,9,500]）;
# Benz = Car(“奔驰”，[80,7,600]);
# 打印结果：
# 宝马：60，4500
# 奔驰：80，4200
# 宝马的价格更便宜，奔驰的损耗值较低

class Car(object):
    def __init__(self, name, price, loss, mile):
        self.name = name
        self.loss = [price, loss, mile]

    def getName(self):
        return self.name

    def getPrice(self):
        return self.loss[0]

    def getLoss(self):
        return self.loss[1] * self.loss[2]


Bmw = Car("宝马", 60, 9, 500)
Benz = Car("奔驰", 80, 7, 600)

name = Bmw.getName()
price = Bmw.getPrice()
loss = Bmw.getLoss()

name2 = Benz.getName()
price2 = Benz.getPrice()
loss2 = Benz.getLoss()

print('名字:%s, 价格:%d, 油耗:%d' % (name, price, loss))
print('名字:%s, 价格:%d, 油耗:%d' % (name2, price2, loss2))
if price > price2:
    print('%s的价格更低' % name2)
else:
    print('%s的价格更低' % name)
if loss > loss2:
    print('%s的油耗更低' % name2)
else:
    print('%s的油耗更低' % name)