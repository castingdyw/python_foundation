# 定义类：枪，玩家
# 枪：属性：型号，杀伤力，子弹数。 方法：添加子弹，射击，
# 玩家：属性：姓名，血量。 方法:拿枪，让枪射击，中弹掉血


class Gun(object):
    """枪类"""
    def __init__(self, model, damage):
        """初始化参数"""
        self.model = model
        self.damage = damage
        self.bullet = 0

    def __str__(self):
        """返回枪的描述信息"""
        return '%s 的杀伤力是 %s ，剩余子弹数有 %s' % (self.model, self.damage, self.bullet)

    def add_bullet(self, count):
        """添加子弹"""
        self.bullet += count

    def shoot(self, enemy):
        """射击敌人"""
        if self.bullet <= 0:
            print('没有子弹了')
            return
        self.bullet -= 1
        # print('%s 射中了 %s ，造成 %s 伤害' % (self.model, enemy, self.damage))
        enemy.hurt(self.damage)


class Player(object):
    """定义玩家类"""
    def __init__(self, name, hp):
        """初始化参数"""
        self.name = name
        self.hp = hp
        self.gun = None

    def __str__(self):
        """打印玩家信息"""
        if self.hp <= 0:
            return '血量低于0，玩家死亡'
        if self.gun == None:
            return '玩家 %s 目前血量 %s ，目前没有枪' % (self.name, self.hp)
        return '玩家 %s 目前血量 %s ,目前有枪[%s]' % (self.name, self.hp, self.gun)

    def take_gun(self, gun):
        """拿枪"""
        self.gun = gun

    def fire(self, enemy):
        """射击敌人"""
        # print('玩家 %s 使用 [%s] 开枪射击了 [%s] ' % (self.name, self.gun, enemy))
        # enemy.hurt(89)
        self.gun.shoot(enemy)

    def hurt(self, damage):
        """中弹掉血"""
        self.hp -= damage
        print(self)


def main():
    # 生成枪
    k98 = Gun('98k', 40)
    print(k98)

    # 生成玩家
    plice = Player('警察', 100)
    print(plice)
    badman = Player('土匪', 100)
    print(badman)

    # 玩家拿枪
    plice.take_gun(k98)
    print(plice)

    # 添加子弹
    k98.add_bullet(5)
    print(plice)

    # 开枪射击
    plice.fire(badman)




main()