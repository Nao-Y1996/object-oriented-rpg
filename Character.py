
class character:
    # キャラクターの持つ変数
    def __init__(self, name, hp=100, power=10, characterType="nomal"):
        self.name = name
        self.hp = hp
        self.power = power
        self.weapon = None
        self.characterType = characterType
        print(f"{self.name}が現れた！")
    
    # キャラクターは武器を装備できる
    def setWeapon(self,weapon):
        self.weapon = weapon
        print(f"{self.name}は「{weapon.name}」を装備した！")

    # キャラクターは攻撃ができる
    # enemyにはcharacterクラスのオブジェクトを入れる
    def attackTo(self,enemy):
        print(f"{self.name}から{enemy.name}への攻撃")
        # 自分の攻撃力分相手のHPを下げる
        enemy.hp -= self.power
        # 敵のHPを表示
        print(f"{enemy.name}のHPは{enemy.hp}になった！")
        

