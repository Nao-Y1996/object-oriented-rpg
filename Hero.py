from Character import character
# キャラクタークラスを継承した「勇者クラス」
class hero(character):

    def __init__(self, name):
        # 勇者はhp=150, power=15, type="hero"のキャラクター
        super().__init__(name, hp=150, power=15, characterType="hero")

    # 勇者は特殊攻撃ができる
    def specialAttackTo(self, enemy):
        # 今の攻撃力を保持
        power = self.power

        # 武器を持っていて、その武器のタイプが自身と同じheroであれば、一時的に攻撃力をあげる
        if(self.weapon is not None and self.weapon.weaponType == self.characterType):
            self.power += self.weapon.powerUp
            print(f"特殊攻撃ができる！　武器「{self.weapon.name}」によって攻撃力が上がった！")
        else:
            print(f"{self.name}は今特殊攻撃ができない！")

        # ただし敵が武器を持っていたら、その武器の防御力分だけ攻撃力が落ちる
        if (enemy.weapon is not None):
            self.power -= enemy.weapon.defenceUp
            print(f"{enemy.name}は武器「{enemy.weapon.name}」を持っている！攻撃力が下がった！")

        # 攻撃力が上がった状態で攻撃を行う（キャラクタークラスのattackToメソッドを使う）
        super().attackTo(enemy)

        # 一時的に変化した攻撃力を元に戻す
        self.power = power
