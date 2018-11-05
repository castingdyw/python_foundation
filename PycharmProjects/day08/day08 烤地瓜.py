class SweetPotato:
    def __init__(self):
        self.cook_level = 0
        self.cook_string = '生的'
        self.cookcondiments = []

    def __str__(self):
        return '这个地瓜目前%s熟，状态是%s,添加的调料有%s' % (self.cook_level, self.cook_string, self.cookcondiments)

    # 修改描述信息
    # 0~3表示还是生的，超过3表示半生不熟，超过5表示已经烤好了，超过8表示已经烤成木炭了！
    def cook(self, time):
        self.cook_level += time
        if self.cook_level <= 3:
            self.cook_string = '生的'
        elif self.cook_level <= 5:
            self.cook_string = '半生不熟'
        elif self.cook_level <= 8:
            self.cook_string = '烤好了'
        else:
            self.cook_string = '已经烤成木炭了'

    def add_condiments(self, item):
        self.cookcondiments.append(item)

potato = SweetPotato()
print(potato)
potato.cook(4)
print(potato)
potato.cook(2)
potato.add_condiments('辣椒')
print(potato)


# class SweetPotato(object):  # 烤地瓜自己的方法
#
#     def __init__(self):
#         self.cook_level = 0
#         self.cook_string = '生的'
#         self.cook_add = []
#         self.time = 0
#
#     def __str__(self):
#         return '已经烤了%s分钟,烧烤等级为%s,烧烤状态为%s,添加的佐料有%s' % (self.time, self.cook_level, self.cook_string, self.cook_add)
#
#     def cook_time(self, time):
#         self.time += time
#         if self.time <= 3:
#             self.cook_level = 1
#             self.cook_string = '烤熟一半'
#         elif self.time <= 6:
#             self.cook_level = 2
#             self.cook_string = '已经烤熟了'
#         elif self.time >= 6:
#             self.cook_level = 3
#             self.cook_string = '已经烤烂了'
#
#     def cook_condi(self, add):
#         self.cook_add.append(add)
#
# p = SweetPotato()
# print(p)
# p.cook_time(2)
# print(p)
# p.cook_time(2)
# print(p)
# p.cook_condi('辣椒')
# print(p)