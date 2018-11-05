class House:
    def __init__(self, area):
        self.area = area
        self.items = []

    def __str__(self):
        name = ''
        for i in self.items:
            name += i.type + ','
        return '房子大小 %s, --%s' % (self.area, name)

    def add_bed(self, item):
        self.items.append(item)
# House类里面调用Bed类的信息，House里面添加属性，调用方法时对象bed当作参数传递
class Bed:
    def __init__(self, type, size):
        self.type = type
        self.size = size

    def __str__(self):
        return '%s 床的大小是 %s' % (self.type, self.size)


house = House(300)
# print(house)

bed = Bed('席梦思', 10)
bed1 = Bed('寒冰床', 20)
house.add_bed(bed)
house.add_bed(bed1)

print(house)
