from Weapon import weapon
# 武器クラスを継承した「鋼の剣」クラス
class steelSword(weapon):
    def __init__(self, name):
        # 鋼の剣はpowerUp=5, defenceUp=2の武器
        super().__init__(name, powerUp=5, defenceUp=2, weaponType="hero")
