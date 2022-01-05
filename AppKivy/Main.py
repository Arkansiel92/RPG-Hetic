from os import remove
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.animation import Animation
from random import randint

from kivy.uix.widget import Widget
from Class_characters import *

Builder.load_file('Main.kv')

map1 = [[],[],[],
       [],[],[],
       [],[],[]]



class Main(Screen): # Ecran principal/choix
    list_sound = ['divers/music/dungeon-quest-ost-track2.mp3', 'divers/music/enchanted-forest.mp3',
        'divers/music/dungeon-quest-ost.mp3'] # Liste des musiques du jeu 
    music = SoundLoader.load('divers/music/dungeon-quest-ost.mp3')
    music.loop = True
    if music:
        music.play()
    def sound(self, switchObject, switchValue):
        if switchValue:
            print("[Terminal] : play music")
            self.music.play()
        else:
            print("[Terminal] : stop music")
            self.music.stop()


class Info(Screen): # Ecran à propos
    pass

class Load(Screen): # Ecran de chargement de parties
    pass

class Play(Screen): # Ecran de création du personnage
    i = 0 # incrémentation pour le choix du skin
    List_Skin = ["Img/Player.png","Img/Player_2.png","Img/Player_3.png","Img/Player_4.png"]
    List_class = ["Classe : Heros","Classe : Berserk","Classe : Magicienne","Classe : Garde"]
    remaining_points = NumericProperty(10)

    def skin_player_right(self): # fonction choix du skin
        skin = self.ids.skin_perso
        class_player = self.ids.class_player
        if self.i <= 2:
            skin.source = self.List_Skin[self.i + 1]
            class_player.text = self.List_class[self.i + 1]
            self.i += 1
            if self.List_class[self.i] == "Classe : Heros":
                Player_Main1.health = 250
                Player_Main1.strength = 50
                Player_Main1.defense = 50
                Player_Main1.mana = 100
            elif self.List_class[self.i] == "Classe : Berserk":
                Player_Main1.health = 200
                Player_Main1.strength = 100
                Player_Main1.defense = 80
                Player_Main1.mana = 50
            elif self.List_class[self.i] == "Classe : Magicienne":
                Player_Main1.health = 200
                Player_Main1.strength = 50
                Player_Main1.defense = 50
                Player_Main1.mana = 200
            elif self.List_class[self.i] == "Classe : Garde":
                Player_Main1.health = 300
                Player_Main1.strength = 50
                Player_Main1.defense = 150
                Player_Main1.mana = 50
            self.remaining_points = 10
            self.ids.counter_health.text= str(Player_Main1.health)
            self.ids.counter_strength.text= str(Player_Main1.strength)
            self.ids.counter_defense.text= str(Player_Main1.defense)
            self.ids.counter_magic.text= str(Player_Main1.mana)
            self.ids.remaining_counter.text= str(self.remaining_points)


    def skin_player_left(self): # fonction choix du skin
        skin = self.ids.skin_perso
        class_player = self.ids.class_player
        if self.i > 0:
            skin.source = self.List_Skin[self.i - 1]
            class_player.text = self.List_class[self.i - 1]
            self.i -= 1
            if self.List_class[self.i] == "Classe : Heros":
                Player_Main1.health = 250
                Player_Main1.strength = 50
                Player_Main1.defense = 50
                Player_Main1.mana = 100
            elif self.List_class[self.i] == "Classe : Berserk":
                Player_Main1.health = 200
                Player_Main1.strength = 100
                Player_Main1.defense = 80
                Player_Main1.mana = 50
            elif self.List_class[self.i] == "Classe : Magicienne":
                Player_Main1.health = 200
                Player_Main1.strength = 50
                Player_Main1.defense = 50
                Player_Main1.mana = 200
            elif self.List_class[self.i] == "Classe : Garde":
                Player_Main1.health = 300
                Player_Main1.strength = 50
                Player_Main1.defense = 150
                Player_Main1.mana = 50
            self.remaining_points = 10
            self.ids.counter_health.text= str(Player_Main1.health)
            self.ids.counter_strength.text= str(Player_Main1.strength)
            self.ids.counter_defense.text= str(Player_Main1.defense)
            self.ids.counter_magic.text= str(Player_Main1.mana)
            self.ids.remaining_counter.text= str(self.remaining_points)

    def add_health(self, *args): # fonction ajout vie
        if self.remaining_points > 0:
            self.remaining_points -= 1
            Player_Main1.health += 20
            self.ids.counter_health.text= str(Player_Main1.health)
            self.ids.remaining_counter.text= str(self.remaining_points)
            print("[Terminal] : 20 points de vie ajouté.")
        return Player_Main1.health

    def add_strength(self, *args): # fonction ajout force
        if self.remaining_points > 0:
            self.remaining_points -= 1
            Player_Main1.strength += 5
            self.ids.counter_strength.text= str(Player_Main1.strength)
            self.ids.remaining_counter.text= str(self.remaining_points)
            print("[Terminal] : 5 points de force ajouté.")
        return Player_Main1.strength

    def add_defense(self, *args): # fonction ajout defense
        if self.remaining_points > 0:
            self.remaining_points -= 1
            Player_Main1.defense += 5
            self.ids.counter_defense.text= str(Player_Main1.defense)
            self.ids.remaining_counter.text= str(self.remaining_points)
            print("[Terminal] : 5 points de défense ajouté.")
        return Player_Main1.defense

    def add_magic(self, *args): # fonction ajout magie
        if self.remaining_points > 0:
            self.remaining_points -= 1
            Player_Main1.mana += 10
            self.ids.counter_magic.text= str(Player_Main1.mana)
            self.ids.remaining_counter.text= str(self.remaining_points)
            print("[Terminal] : 10 points de magie ajouté.")
        return Player_Main1.mana

    def restart_caract(self, *args): # remet à zéro les caracts
        if self.List_class[self.i] == "Classe : Heros":
            Player_Main1.health = 250
            Player_Main1.strength = 50
            Player_Main1.defense = 50
            Player_Main1.mana = 100
        elif self.List_class[self.i] == "Classe : Berserk":
            Player_Main1.health = 200
            Player_Main1.strength = 100
            Player_Main1.defense = 80
            Player_Main1.mana = 50
        elif self.List_class[self.i] == "Classe : Magicienne":
            Player_Main1.health = 200
            Player_Main1.strength = 50
            Player_Main1.defense = 50
            Player_Main1.mana = 200
        elif self.List_class[self.i] == "Classe : Garde":
            Player_Main1.health = 300
            Player_Main1.strength = 50
            Player_Main1.defense = 150
            Player_Main1.mana = 50
        self.remaining_points = 10
        self.ids.counter_health.text= str(Player_Main1.health)
        self.ids.counter_strength.text= str(Player_Main1.strength)
        self.ids.counter_defense.text= str(Player_Main1.defense)
        self.ids.counter_magic.text= str(Player_Main1.mana)
        self.ids.remaining_counter.text= str(self.remaining_points)
        print("[Terminal] : réinitialisation des points de caractéristiques.")
    
    def print(self, *args): # définition du nom du joueur
        name = self.ids.name_of_player
        Player_Main1.name = str(name.text)
        print("[Terminal] : nom du joueur :", str(name.text))
        skin = self.ids.skin_perso
        Player_Main1.skin = str(skin.source)


class Story(Screen): # Ecran du jeu  
    # variable map du jeu
    icon_player = ObjectProperty(None)
    Player_map = "옷"
    pos_player = 4
    map1[pos_player].append(Player_map)

    def changeScreen(self, *args):
        self.parent.current = "FightWindow"
    
    def changeDungeon(self, *args):
        self.parent.current = "Dungeon"

    def fight(self): # check si le combat est déjà fait selon la position
        if self.pos_player == 1 and 'Gros nounours' not in Player_Main1.monster_dead or self.pos_player == 2 and 'Brontis' not in Player_Main1.monster_dead or self.pos_player == 5 and 'Loic' not in Player_Main1.monster_dead or self.pos_player == 7 and 'Les impots' not in Player_Main1.monster_dead:
            Clock.schedule_once(self.changeScreen, .5)
        elif self.pos_player == 8:
            Clock.schedule_once(self.changeDungeon, .5)
        return

    def run_nord(self): # fonction pour aller au nord
        map1[self.pos_player].remove(self.Player_map)
        text = self.ids.text_direction
        text.text ="Quelle direction voulez-vous prendre ?"
        if self.pos_player == 3:
            self.pos_player = self.pos_player - 3
            self.icon_player.pos = -130, 140
        elif self.pos_player == 4:
            self.pos_player = self.pos_player - 3
            self.icon_player.pos = 0, 150
        elif self.pos_player == 5:
            self.pos_player = self.pos_player - 3
            self.icon_player.pos = 160, 150
        elif self.pos_player == 6:
            self.pos_player = self.pos_player - 3
            self.icon_player.pos = -130, 0
        elif self.pos_player == 7:
            self.pos_player = self.pos_player - 3
            self.icon_player.pos = 0, 0
        elif self.pos_player == 8:
            self.pos_player = self.pos_player - 3
            self.icon_player.pos = 160, 0
        else:
            text.text ="Aucun chemin dans cette direction..."  
        map1[self.pos_player].append(self.Player_map)
        Player_Main1.pos = self.pos_player
        self.fight()

    def run_sud(self): # fonction pour aller au sud
        map1[self.pos_player].remove(self.Player_map)
        text = self.ids.text_direction
        text.text ="Quelle direction voulez-vous prendre ?"
        if self.pos_player == 0:
            self.pos_player = self.pos_player + 3
            self.icon_player.pos = -130, 0
        elif self.pos_player == 1:
            self.pos_player = self.pos_player + 3
            self.icon_player.pos = 0, 0
        elif self.pos_player == 2:
            self.pos_player = self.pos_player + 3
            self.icon_player.pos = 160, 0
        elif self.pos_player == 3:
            self.pos_player = self.pos_player + 3
            self.icon_player.pos = -130, -140
        elif self.pos_player == 4:
            self.pos_player = self.pos_player + 3
            self.icon_player.pos = 0, -140
        elif self.pos_player == 5:
            self.pos_player = self.pos_player + 3
            self.icon_player.pos = 160, -140
        else:
            text.text ="Aucun chemin dans cette direction..."  
        map1[self.pos_player].append(self.Player_map)
        Player_Main1.pos = self.pos_player
        self.fight()

    def run_ouest(self): # fonction pour aller à l'ouest
        map1[self.pos_player].remove(self.Player_map)
        text = self.ids.text_direction
        text.text ="Quelle direction voulez-vous prendre ?"
        if self.pos_player == 1:
            self.pos_player = self.pos_player - 1
            self.icon_player.pos = -130, 140
        elif self.pos_player == 2:
            self.pos_player = self.pos_player - 1
            self.icon_player.pos = 0, 150
        elif self.pos_player == 4:
            self.pos_player = self.pos_player - 1
            self.icon_player.pos = -130, 0
        elif self.pos_player == 5:
            self.pos_player = self.pos_player - 1
            self.icon_player.pos = 0, 0
        elif self.pos_player == 7:
            self.pos_player = self.pos_player - 1
            self.icon_player.pos = -130, -140
        elif self.pos_player == 8:
            self.pos_player = self.pos_player - 1
            self.icon_player.pos = 0, -140
        else:
            text.text ="Aucun chemin dans cette direction..."  
        map1[self.pos_player].append(self.Player_map)
        Player_Main1.pos = self.pos_player
        self.fight()

    def run_est(self): # fonction pour aller à l'est
        map1[self.pos_player].remove(self.Player_map)
        text = self.ids.text_direction
        text.text ="Quelle direction voulez-vous prendre ?"
        if self.pos_player == 0:
            self.pos_player = self.pos_player + 1
            self.icon_player.pos = 0, 150
        elif self.pos_player == 1:
            self.pos_player = self.pos_player + 1
            self.icon_player.pos = 160, 150
        elif self.pos_player == 3:
            self.pos_player = self.pos_player + 1
            self.icon_player.pos = 0, 0
        elif self.pos_player == 4:
            self.pos_player = self.pos_player + 1
            self.icon_player.pos = 160, 0
        elif self.pos_player == 6:
            self.pos_player = self.pos_player + 1
            self.icon_player.pos = 0, -140
        elif self.pos_player == 7:
            self.pos_player = self.pos_player + 1
            self.icon_player.pos = 160, -140
        else:
            text.text ="Aucun chemin dans cette direction..."  
        map1[self.pos_player].append(self.Player_map)
        Player_Main1.pos = self.pos_player
        self.fight()
        


class Fight(Screen):  #Ecran de combat
    # Variable string
    monster = None
    health_player = StringProperty("")
    mana_player = StringProperty("")
    level = StringProperty(str(Player_Main1.level))
    skin = StringProperty('Img/Player.png')
    monster_health = StringProperty("")
    skin_monster = StringProperty("")
    potion_1 = randint(1, 3)
    potion_2 = randint(1, 3)
    potion_3 = randint(1, 3)
    # Variable widget
    text_monster = ObjectProperty(None)
    choice_action = ObjectProperty(None)
    choice_spell = ObjectProperty(None)
    button_yes = ObjectProperty(None)
    button_no = ObjectProperty(None)
    name_monster = ObjectProperty(None)

    def choose_monster(self, *args):
        if Player_Main1.pos == 1:
            return Gros_nounours
        elif Player_Main1.pos == 2:
            return Brontis
        elif Player_Main1.pos == 5:
            return Loic
        elif Player_Main1.pos == 7:
            return Les_impots

    

    
    def Anime_spell(self, widget): # Animation des sorts
        Anime_spell = Animation(opacity=1, duration=.2)
        Anime_spell.start(widget)
        if widget == self.ids.gif_fire or widget == self.ids.gif_thunder: # Animation sorts de dégats
            widget.pos = -300, -400
            Anime_spell = Animation(x=430, y=-420)
            Anime_spell.start(widget)
            Anime_spell += Animation(opacity=0, duration=.1)
            Anime_spell.start(widget)
        elif widget == self.ids.gif_bravoure or widget == self.ids.gif_ataraxie: # Animation sorts de boost
            widget.pos = -400, -430
            Anime_spell += Animation(opacity=0, duration=.1)
            Anime_spell.start(widget)
        elif widget == self.ids.gif_monster: # Animation sort du monstre
            widget.pos = -400, -400
            Anime_spell += Animation(opacity=0, duration=.1)
            Anime_spell.start(widget)




    def menu_fight(self): # menu d'action
        self.choice_spell.pos=0, 2000
        self.choice_action.pos=0, 200

    def attack_weapon(self): # attaque avec l'arme de base
        self.choice_action.pos=0, 2000
        self.text_monster.text ="%s attaque avec son arme ! -%s a l'adversaire !"%(Player_Main1.name, Player_Main1.strength)
        self.monster.health = self.monster.health - Player_Main1.strength
        self.monster_health = str(self.monster.health)
        Clock.schedule_once(self.monster_turn, 2)
        print("[Terminal] Fin du tour du joueur.")

    def choose_spell(self): # choix du sort
        self.choice_action.pos=0, 2000
        self.text_monster.text ="Quel sort voulez-vous lancer ?"
        self.choice_spell.pos=0, 200

    def Fire_Spell(self):
        if Player_Main1.mana > Spell_Feu.mana:
            self.text_monster.text="%s lance le Souffle de feu ! -%s a l'adversaire !"%(Player_Main1.name, Spell_Feu.effect)
            self.choice_spell.pos=0, 2000
            Player_Main1.mana = Player_Main1.mana - Spell_Feu.mana
            self.monster.health = self.monster.health - Spell_Feu.effect
            self.Anime_spell(self.ids.gif_fire)
            self.monster_health = str(self.monster.health)
            self.mana_player = str(Player_Main1.mana)
            Clock.schedule_once(self.monster_turn, 2)
        else:
            self.text_monster.text="Il vous faut plus de mana !"

    def Thunder_Spell(self):
        if Player_Main1.mana > Spell_Eclair.mana:
            self.text_monster.text="%s lance l'eclair pourfendeur ! -%s a l'adversaire !"%(Player_Main1.name, Spell_Eclair.effect, )
            self.choice_spell.pos=0, 2000
            Player_Main1.mana = Player_Main1.mana - Spell_Eclair.mana
            self.monster.health = self.monster.health - Spell_Eclair.effect
            self.Anime_spell(self.ids.gif_thunder)
            self.monster_health = str(self.monster.health)
            self.mana_player = str(Player_Main1.mana)
            Clock.schedule_once(self.monster_turn, 2)
        if self.monster.health < 0:
            self.monster.health = 0
        else:
            self.text_monster.text="Il vous faut plus de mana !"

    def Protect_Spell(self):
        if Player_Main1.mana > Spell_Ataraxie.mana:
            self.text_monster.text="%s lance Ataraxie ! +%s HP !"%(Player_Main1.name, Spell_Ataraxie.effect)
            self.choice_spell.pos=0, 2000
            Player_Main1.mana = Player_Main1.mana - Spell_Ataraxie.mana
            Player_Main1.health = Player_Main1.health + Spell_Ataraxie.effect
            self.Anime_spell(self.ids.gif_ataraxie)
            self.health_player = str(Player_Main1.health)
            self.mana_player = str(Player_Main1.mana)
            Clock.schedule_once(self.monster_turn, 2)
        else:
            self.text_monster.text="Il vous faut plus de mana !"

    def Boost_Spell(self):
        self.text_monster.text="%s lance Bravoure ! +%s mana !"%(Player_Main1.name, Spell_Bravoure.effect)
        self.choice_spell.pos=0, 2000
        Player_Main1.mana = Player_Main1.mana + Spell_Bravoure.effect
        self.Anime_spell(self.ids.gif_bravoure)
        self.mana_player = str(Player_Main1.mana)
        Clock.schedule_once(self.monster_turn, 2)

        
    
    def attack_system(self, *args): # choix du joueur
        if self.monster == None: # choix du monstre
            self.monster = self.choose_monster(*args)
        # caract du personnage
        self.name_monster.text = self.monster.name
        if Player_Main1.health > 0:
            skin_player = self.ids.skin_player
            skin_monster = self.ids.skin_monster
            self.health_player = str(Player_Main1.health)
            self.mana_player = str(Player_Main1.mana)
            self.skin = Player_Main1.skin
            self.monster_health = str(self.monster.health)
            self.skin_monster = self.monster.skin
            self.text_monster.text = "Que voulez-vous faire ?"

            # mettre à jour les widgets
            skin_player.pos = -400, -380
            skin_monster.pos = 400, -380
            self.button_yes.pos = 0, 2000
            self.button_no.pos = 0, 2000
            self.choice_action.pos =0, 200
        else:
            skin_player = self.ids.skin_player
            skin_player.pos = 0, 2000
            self.fight_end()

    def monster_turn(self, *args): # tour du monstre
        if self.monster.health > 0:
            self.choice_action.pos=0, 2000
            self.text_monster.text ="Le monstre attaque ! -%s HP sur %s !"%(self.monster.attack, Player_Main1.name)
            Player_Main1.health = Player_Main1.health - self.monster.attack
            self.Anime_spell(self.ids.gif_monster)
            self.health_player = str(Player_Main1.health)
            Clock.schedule_once(self.attack_system, 2)
        else:
            skin_monster = self.ids.skin_monster
            skin_monster.pos = 0, 2000
            self.fight_end()

    def fight_end(self): # fin du combat
        print("[Terminal] Fin du combat.")
        menu_end = self.ids.end_fight
        text_xp = self.ids.xp_text
        button = self.ids.button_end_fight
        self.text_monster.text=""
        menu_end.pos = 0, 0
        text_xp.pos=0, 100
        button.pos=900, 250
        self.potion_1 = randint(1, 3)
        self.potion_2 = randint(1, 3)
        self.potion_3 = randint(1, 3)
        if Player_Main1.health > 0:
            text_xp.text="Vous avez gagne %s points d'experience ! \nVous venez de drop :"%(self.monster.xp)
            if self.potion_1 == 1:
                self.potion_1 = self.ids.low_potion_health
                self.potion_1.pos=-180, -100
                Player_Main1.inventory.append("Potion faible de vie")
                print("Drop petite potion de soin")
            elif self.potion_1 == 2:
                self.potion_1 = self.ids.medium_potion_health
                print("Drop moyenne potion de soin")
                self.potion_1.pos=-180, -100
                Player_Main1.inventory.append("Potion moyenne de vie")
            elif self.potion_1 == 3:
                self.potion_1 = self.ids.strong_potion_health
                print("Drop forte potion de soin")
                self.potion_1.pos=-180, -100
                Player_Main1.inventory.append("Potion forte de vie")
            if self.potion_2 == 1:
                self.potion_2 = self.ids.low_potion_mana
                print("Drop petite potion de mana")
                self.potion_2.pos=0, -100
                Player_Main1.inventory.append("Potion faible de mana")
            elif self.potion_2 == 2:
                self.potion_2 = self.ids.medium_potion_mana
                print("Drop moyenne potion de mana")
                self.potion_2.pos=0, -100
                Player_Main1.inventory.append("Potion moyenne de mana")
            elif self.potion_2 == 3:
                self.potion_2 = self.ids.strong_potion_mana
                print("Drop forte potion de mana")
                self.potion_2.pos=0, -100
                Player_Main1.inventory.append("Potion forte de mana")
            if self.potion_3 == 1:
                self.potion_3 = self.ids.low_potion_strength
                print("Drop petite potion de force")
                self.potion_3.pos=180, -100
                Player_Main1.inventory.append("Potion faible de force")
            elif self.potion_3 == 2:
                self.potion_3 = self.ids.medium_potion_strength
                print("Drop moyenne potion de force")
                self.potion_3.pos=180, -100
                Player_Main1.inventory.append("Potion moyenne de force")
            elif self.potion_3 == 3:
                self.potion_3 = self.ids.strong_potion_strength
                print("Drop forte potion de force")
                self.potion_3.pos=180, -100
                Player_Main1.inventory.append("Potion forte de force")
        else:
            text_xp.text ="Vous avez perdu !"

    def refresh(self):
        # définition des variables
        self.text_monster.text="Un monstre n'est pas loin ! Voulez-vous l'attaquer ?"
        image_endfight = self.ids.end_fight
        button_endfight = self.ids.button_end_fight
        xp_text = self.ids.xp_text
        skin_player = self.ids.skin_player
        skin_monster = self.ids.skin_monster
        # repositionnement des widgets
        xp_text.pos = 0, 2000
        image_endfight.pos = 0, 2000
        button_endfight.pos = 0, 2000
        self.button_yes.pos = 600, 800
        self.button_no.pos = 1100, 800
        skin_player.pos = 0, 2000
        skin_monster.pos = 0, 2000
        if Player_Main1.health > 0: # vérifier si le combat est gagné.
            self.potion_1.pos = 0, 2000
            self.potion_2.pos = 0, 2000
            self.potion_3.pos = 0, 2000
        Player_Main1.monster_dead.append(self.monster.name)
        self.monster = None
        print("[Terminal] Fin du combat.")

class Dungeon(Screen):

    def Dungeon(self):
        bg = self.ids.dungeon_background
        text = self.ids.dungeon_text
        bg.source = 'Img/Background/background_dungeon.jpg'
        button = self.ids.enter_button
        self.remove_widget(button)
        text.font_size = 68
        text.text = 'En cours de debug...(sorry)'



# class config de lancement
class Myapp(App):
    title = "RPGTic - Python Game"
    def build(self):
        Window.fullscreen = 'auto'
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(Main(name='MainWindow'))
        sm.add_widget(Info(name='InfoWindow'))
        sm.add_widget(Load(name='LoadWindow'))
        sm.add_widget(Play(name='NewGame'))
        sm.add_widget(Story(name='StoryWindow'))
        sm.add_widget(Fight(name='FightWindow'))
        sm.add_widget(Dungeon(name='Dungeon'))
        return sm

if __name__ == "__main__":
    Myapp().run()