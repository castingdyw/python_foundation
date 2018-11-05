# 定义一个汽车类
#     * 在类中定义一个move方法打印'汽车在移动'
#     * 分别创建BMW_X9、AUDI_A9对象
#     * 最后调用move方法。
# class car:
#     def move(self):
#         print('汽车在移动')
#
# BMW_X9 = car()
# AUDI_A9 = car()
# BMW_X9.move()
# AUDI_A9.move()

# 定义一个People类
#     * 使用People类创建一个mayun对象添加company属性，值是"阿里巴巴"；
#     * 创建一个wangjianlin对象，添加company属性，值是"万达集团";
#     * 打印两个对象的 company 值。
#     (注意：不要使用 init 方法)
# class People:
#     def com(self):
#         print(self.company)
#
# mayun = People()
# mayun.company = '阿里巴巴'
#
# wanjianlin = People()
# wanjianlin.company = '万达集团'
#
# mayun.com()
# wanjianlin.com()
#
# print(mayun.company)

# 5. 定义一个汽车类
#     * 在类中定义一个move方法打印'汽车在移动'
#     * 分别创建BMW_X9、AUDI_A9对象
#     * 并添加颜色、型号等属性，然后打印出属性值
#     (注意：不要使用 init 方法)
class Car:
    def move(self):
        print('汽车在移动')
        print('颜色%s,型号%s' % (self.color, self.type))

BMW_X9 = Car()
BMW_X9.color = 'red'
BMW_X9.type = 'A'
BMW_X9.move()

AUDI_A9 = Car()
AUDI_A9.color = 'green'
AUDI_A9.type = 'B'

