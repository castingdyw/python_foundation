class House(object):
    def __init__(self, area):
        self.area = area
    def __str__(self):
        return '房子面积%d-- %s' % (self.area, self.size)
    def get_bed(self, item):
        self.size = item
    def get_sleep(self, item):
        print('房子')
        item.sleep()  # 调用另一个类的方法
        print(item.size)

class Bed(object):
    def __init__(self, size):
        self.size = size
    def __str__(self):
        return '床的大小%d' % self.size
    def sleep(self):
        print('床能睡觉')

house = House(100)
bed = Bed(20)
# house.get_bed(bed)
# print(house)
# bed.sleep()
house.get_sleep(bed)