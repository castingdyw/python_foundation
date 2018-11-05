class House:
    def __init__(self, area):
        self.area = area
        self.items = []

    def __str__(self):
        name = ''
        for item in self.items:
            name += str(item) + ', '
        return '房子大小 %s, --%s' % (self.area,name)

    def add_bed(self, items):
        self.items.append(items)

class Bed:
    def __init__(self, type, size):
        self.type = type
        self.size = size

    def __str__(self):
        return '%s 床的大小是 %s' % (self.type, self.size)

class Bed2:
    def __init__(self, type, size):
        self.type = type
        self.size = size

    def __str__(self):
        return '%s 床的大小是 %s' % (self.type, self.size)

house = House(300)
# print(house)

bed = Bed('席梦思', 10)
print(bed)

bed2 = Bed2('木床', 20)
print(bed)

house.add_bed(bed)
house.add_bed(bed2)
print(house)
