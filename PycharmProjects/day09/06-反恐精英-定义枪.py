# 定义两个类，枪和玩家，玩家有两个对象，警察和土匪
# 枪，属性：型号，杀伤力，剩余子弹数量。方法：添加子弹，射击
# 玩家，属性：姓名，血量。方法：拿枪，让枪射击，掉血


class Gun(object):
    """枪类"""
    def __init__(self, model, damage):
        """初始化枪的属性"""
        self.model = model
        self.damage = damage
        self.bullet_count = 0

    def __str__(self):
        """返回枪的描述信息"""
        return '%s 的枪的杀伤力是 %d, 剩余子弹数%d' % (self.model, self.damage, self.bullet_count)

    def add_bullet(self, count):
        """添加子弹"""
        self.bullet_count += count

    def shoot(self, enemy):
        """射击敌人"""
        if self.bullet_count <= 0:
            print('没有子弹了')
            return
        """减少子弹"""
        self.bullet_count -= 1
        print('%s射中%s,造成%d伤害' % (self.model, enemy, self.damage))






class Player(object):
    """玩家类"""
    pass



def test():
    """测试枪"""
    """生成枪"""
    gun = Gun('ak47',90)
    print(gun)
    """添加子弹"""
    gun.add_bullet(10)
    print(gun)
    """造成伤害"""
    gun.shoot('张三')
    print(gun)
    gun.shoot('张三')
    print(gun)

test()
