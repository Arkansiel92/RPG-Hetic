from random import randint

class Player_Main:
    def __init__(self, name, health, strength, defense, mana, xp, level, skin, pos):
        self.name = name
        self.health = health 
        self.strength = strength
        self.defense = defense
        self.mana = mana
        self.inventory = []
        self.spells = []
        self.xp = xp
        self.level = level
        self.skin = skin
        self.pos = pos
        self.monster_dead = []
    
    def get_damage(self, damage):
        self.health -= damage
        return self.health

    def get_mana(self, cout_mana):
        self.mana -= cout_mana
        print("Le sort coûte", cout_mana, "en mana ! Il vous reste", self.mana, "de mana !")
        return self.mana

            
class Monster:
    def __init__(self, name, element, health, attack, defense,xp, skin):
        self.name = name
        self.element = element # feu, eau, air, terre
        self.health = health
        self.attack = attack
        self.defense = defense
        self.xp = xp
        self.skin = skin


class Spell:
    def __init__(self, name, effect, mana):
        self.name = name
        self.effect = effect
        self.mana = mana # coût en mana
        
    def damage(self, Monster_health):
        print("Vous lancez", self.name, "!\n")
        print("Le monstre prend", self.damage_spell,"de dégats !")
        Monster_health = Monster_health - self.damage_spell
        return Monster_health
        
    
        

class Weapon:
    def __init__(self, name, type, damage):
        self.name = name
        self.type = type # feu, eau, air, terre
        self.damage = damage

class Potions:
    def __init__(self, name, type, power, ):
        self.name = name
        self.type = type #vie, force, mana
        self.power = power

    def add_caract(self, value_stat):
        return self.power + value_stat 

Player_Main1 = Player_Main("", 250, 50, 50, 100, 0, 1, "Img/Player_2.png", 4)

# ---- class spell
Spell_Feu = Spell("Souffle de feu", 120, 30)
Spell_Eclair = Spell("Eclair Pourfendeur", 150, 60)
Spell_Ataraxie = Spell("Ataraxie", 100, 35)
Spell_Bravoure = Spell("Bravoure", 200, 0)

# ---- class potions
low_health_potion = Potions("Potion faible de vie","vie", 50)
medium_health_potion = Potions("Potion moyenne de vie","vie", 100)
strong_health_potion = Potions("Potion forte de vie","vie", 150)

low_strength_potion = Potions("Potion faible de force","force", 50)
medium_strength_potion = Potions("Potion moyenne de force","force", 100)
strong_strength_potion = Potions("Potion forte de force","force", 150)

low_mana_potion = Potions("Potion faible de mana","mana", 50)
medium_mana_potion = Potions("Potion moyenne de mana","mana", 100)
strong_mana_potion = Potions("Potion forte de mana","mana", 150)

# ---- class weapons
Sword = Weapon("une épée", "acier", 40)
bow = Weapon("un arc", "bois", 35)
magic_wand = Weapon("baguette magique", "feu", 60)

# ---- class Monster                                                                                                                                               
Gros_nounours = Monster("Gros nounours", "terre", 600, 30, 20, 150, "Img/monster_skin2.png")
Brontis = Monster("Brontis", "feu", 800, 40, 30, 300, "Img/monster_skin1.png")
Loic = Monster("Loic", "eau", 1000, 50, 40, 450, "Img/monster_skin2.png")
Les_impots = Monster("Les impots", "air", 1500, 60, 60, 600, "Img/monster_skin1.png")