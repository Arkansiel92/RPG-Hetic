


class Player:
    def __init__(self, health, strength, defense, magic):
        self.health = health 
        self.strength = strength
        self.defense = defense
        self.magic = magic
        self.inventory = []



class Monster:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense