class weapon:

    # 武器の持つ変数
    # 通常武器はpowerUp=1, defenceUp=0
    def __init__(self, name, powerUp=1, defenceUp=0, weaponType="nomal"):
        self.name = name
        self.powerUp = powerUp
        self.defenceUp = defenceUp
        self.weaponType = weaponType
        print(f"武器 : {self.name}が現れた！")