from Weapon import weapon
from Character import character
from Hero import hero
from SteelSword import steelSword

if __name__ == '__main__':
    # 勇者の定義（特殊キャラ）
    hero = hero(name="勇者")
    # 弓使いの定義（通常キャラ）
    archer = character(name="弓使い")

    # 通常武器の定義
    bow1 = weapon(name="弓1")
    bow2 = weapon(name="弓2")

    # 勇者が弓を装備
    hero.setWeapon(bow1)
    # 弓使いが弓を装備
    archer.setWeapon(bow2)

    # スライムの定義（通常キャラ）
    slime1 = character(name="スライム")
    # スライムが勇者に攻撃
    slime1.attackTo(hero)
    # スライムが弓使いに攻撃
    slime1.attackTo(archer)

    hero.specialAttackTo(slime1) # 勇者がスライムに特殊攻撃（結果としては、通常武器を装備しているので通常攻撃になる）
    archer.attackTo(slime1) # 弓使いがスライムに攻撃

    # SteelSwordの定義
    steelSword1 = steelSword(name="鋼の剣")
    # 勇者が「鋼の剣」を装備
    hero.setWeapon(steelSword1)

    hero.specialAttackTo(slime1) # 勇者がスライムに特殊攻撃（結果としては、heroタイプ武器を装備しているので特殊攻撃になる）
    archer.attackTo(slime1) # 弓使いがスライムに攻撃


    
