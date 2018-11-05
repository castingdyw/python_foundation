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
    def __init__(self, name, hp = 100):
        """初始化玩家属性"""
        self.name = name
        self.hp = hp  # 血量
        self.gun = None

    def __str__(self):
        """玩家信息"""
        if self.hp <= 0:
            return '玩家%s已经死亡' % self.name
        if not self.gun:
            return '玩家%s目前血量%d，目前没有枪' % (self.name, self.hp)
        return '玩家%s目前血量%d，目前有枪[%s]' % (self.name, self.hp, self.gun)

    def take_gun(self, gun):
        """玩家拿枪"""
        self.gun = gun

    def fire(self, enemy):
        """玩家开枪"""
        print('玩家%s使用[%s]开枪射击了[%s]' % (self.name, self.gun, enemy))

    def hurt(self, damage):
        """敌人受到伤害,掉血"""
        self.hp -= damage
        print(self)


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
    print('------------------枪测试结束---------------------')
    """测试玩家"""
    """生成警察"""
    pliceman = Player('警察',100)
    print(pliceman)
    """玩家拿枪"""
    pliceman.take_gun('k98')
    print(pliceman)
    """开枪射击"""
    badman = Player('土匪')
    pliceman.fire(badman)
    """受到伤害，玩家掉血"""
    pliceman.hurt(80)

test()
