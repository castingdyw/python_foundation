# class House:
#     def __init__(self, area):
#         self.area = area
#         # self.item = None
#
#     def __str__(self):
#         return '房子大小 %s, --%s' % (self.area, self.item)
#
#     def add_bed(self, item):
#         self.item = item
# # House类里面调用Bed类的信息，House里面添加属性，调用方法时对象bed当作参数传递
# class Bed:
#     def __init__(self, type, size):
#         self.type = type
#         self.size = size
#
#     def __str__(self):
#         return '%s 床的大小是 %s' % (self.type, self.size)
#
# house = House(300)
# # print(house)
#
# bed = Bed('席梦思', 10)
# print(bed)
#
# house.add_bed(bed)
# print(house)



class House:
    def __init__(self, area, item):
        self.area = area
        self.item = item

    def __str__(self):
        return '房子大小 %s, --%s' % (self.area, self.item)

    # def add_bed(self, item):
    #     self.item = item
# House类里面调用Bed类的信息，House里面添加属性，调用方法时对象bed当作参数传递
class Bed:
    def __init__(self, type, size):
        self.type = type
        self.size = size

    def __str__(self):
        return '%s 床的大小是 %s' % (self.type, self.size)

bed = Bed('席梦思', 10)
house = House(300,bed)
print(house.item.type)

