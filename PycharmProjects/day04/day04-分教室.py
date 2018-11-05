import random
#获取数据
teachers = ['aa','bb','cc','dd','ee','ff','gg','hh']
rooms = [[],[],[]]
#随机分教室
#教师往空room里添加
for tea in teachers:
    index = random.randint(0, 2)
    rooms[index].append(tea)
print(rooms)
