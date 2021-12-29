from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.clock import Clock
from kivy.graphics import Rectangle
from random import randint
from time import sleep
from Class_characters import *

Builder.load_file('Main.kv')


Player_Main1 = Player_Main("", 200, 50, 50, 100, 0, 1, "Img/Player_2.png")




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

    def Name(self):
        name = self.ids.name_of_player
        Player_Main1.name = str(name.text)
        return str(name.text)

    def skin_player_right(self):
        skin = self.ids.skin_perso
        class_player = self.ids.class_player
        if self.i <= 2:
            skin.source = self.List_Skin[self.i + 1]
            class_player.text = self.List_class[self.i + 1]
            self.i += 1
            if self.List_class[self.i] == "Classe : Heros":
                Player_Main1.health = 200
                Player_Main1.strength = 50
                Player_Main1.defense = 50
                Player_Main1.mana = 100
            elif self.List_class[self.i] == "Classe : Berserk":
                Player_Main1.health = 100
                Player_Main1.strength = 100
                Player_Main1.defense = 80
                Player_Main1.mana = 50
            elif self.List_class[self.i] == "Classe : Magicienne":
                Player_Main1.health = 150
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


    def skin_player_left(self):
        skin = self.ids.skin_perso
        class_player = self.ids.class_player
        if self.i > 0:
            skin.source = self.List_Skin[self.i - 1]
            class_player.text = self.List_class[self.i - 1]
            self.i -= 1
            if self.List_class[self.i] == "Classe : Heros":
                Player_Main1.health = 200
                Player_Main1.strength = 50
                Player_Main1.defense = 50
                Player_Main1.mana = 100
            elif self.List_class[self.i] == "Classe : Berserk":
                Player_Main1.health = 100
                Player_Main1.strength = 100
                Player_Main1.defense = 80
                Player_Main1.mana = 50
            elif self.List_class[self.i] == "Classe : Magicienne":
                Player_Main1.health = 150
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

    def add_health(self, *args):
        if self.remaining_points > 0:
            self.remaining_points -= 1
            Player_Main1.health += 20
            self.ids.counter_health.text= str(Player_Main1.health)
            self.ids.remaining_counter.text= str(self.remaining_points)
            print("[Terminal] : 20 points de vie ajouté.")
        return Player_Main1.health

    def add_strength(self, *args):
        if self.remaining_points > 0:
            self.remaining_points -= 1
            Player_Main1.strength += 5
            self.ids.counter_strength.text= str(Player_Main1.strength)
            self.ids.remaining_counter.text= str(self.remaining_points)
            print("[Terminal] : 5 points de force ajouté.")
        return Player_Main1.strength

    def add_defense(self, *args):
        if self.remaining_points > 0:
            self.remaining_points -= 1
            Player_Main1.defense += 5
            self.ids.counter_defense.text= str(Player_Main1.defense)
            self.ids.remaining_counter.text= str(self.remaining_points)
            print("[Terminal] : 5 points de défense ajouté.")
        return Player_Main1.defense

    def add_magic(self, *args):
        if self.remaining_points > 0:
            self.remaining_points -= 1
            Player_Main1.mana += 10
            self.ids.counter_magic.text= str(Player_Main1.mana)
            self.ids.remaining_counter.text= str(self.remaining_points)
            print("[Terminal] : 10 points de magie ajouté.")
        return Player_Main1.mana

    def restart_caract(self, *args):
        if self.List_class[self.i] == "Classe : Heros":
            Player_Main1.health = 200
            Player_Main1.strength = 50
            Player_Main1.defense = 50
            Player_Main1.mana = 100
        elif self.List_class[self.i] == "Classe : Berserk":
            Player_Main1.health = 100
            Player_Main1.strength = 100
            Player_Main1.defense = 80
            Player_Main1.mana = 50
        elif self.List_class[self.i] == "Classe : Magicienne":
            Player_Main1.health = 150
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
    
    def print(self, *args):
        name = Play.Name(self)
        print("[Terminal] : nom du joueur :", name)
        text_story = self.ids.text_story
        text_story.pos = 0, 100
        text_story.text = """
    Bienvenue {}. Ton periple debute ici !
    a une epoque ou le mal regnait sur le monde
    et ou l'humanite vivait dans la crainte.
    Un legendaire heros redonna l'espoir au monde
    Vous incarnez le descendant de ce heros. Fier guerrier,
    Vous avez jure de reussir coute que coute,
    et de proteger le monde en tuant l'horrible Brontis.""".format(name)
        button_play = self.ids.go_game
        button_play.pos = 800, 100
        skin = self.ids.skin_perso
        Player_Main1.skin = str(skin.source)

    def beginning(self, widget, *args):
        LayoutGame = self.ids.LayoutGame
        self.remove_widget(LayoutGame)
        Play.print(self)



class Story(Screen): # Ecran du jeu  

    def Clock(self):
        Clock.schedule_once(self.Initialisation)
    
    def Check_inventory(self):
        for i in Player_Main1.inventory:
            if i == "Potion faible de vie":
                print("Une potion faible de vie est ajoutée !")
            elif i == "Potion moyenne de vie":
                print("Une moyenne potion de vie a été ajoutée !")
            elif i == "Potion forte de vie":
                print("Une forte potion de vie a été ajoutée !")

    def Initialisation(self, *args):
        print(self.health_player, Player_Main1.health)
        print(self.mana_player, Player_Main1.mana)


class Fight(Screen):  #Ecran de combat
    # Variable string
    health_player = StringProperty("")
    mana_player = StringProperty("")
    level = StringProperty(str(Player_Main1.level))
    skin = StringProperty("")
    monster_name = StringProperty("")
    monster_health = StringProperty("")
    skin_monster = StringProperty("")
    # Variable widget
    text_monster = ObjectProperty(None)
    choice_action = ObjectProperty(None)
    choice_spell = ObjectProperty(None)

    def menu_fight(self):
        self.remove_widget(self.choice_spell)
        self.add_widget(self.choice_action)

    def attack_weapon(self):
        self.remove_widget(self.choice_action)
        self.text_monster.text ="%s attaque avec son arme !"%(Player_Main1.name)
        Gros_nounours.health = Gros_nounours.health - Player_Main1.strength
        self.monster_health = str(Gros_nounours.health)
        Clock.schedule_once(self.monster_turn, 2)

    def choose_spell(self):
        self.remove_widget(self.ids.choice_action)
        self.text_monster.text ="Quel sort voulez-vous lancer ?"
        self.choice_spell.pos=0, 200
        
    
    def attack_system(self):
        Main.music.stop() 
        # caract du personnage
        self.health_player = str(Player_Main1.health)
        self.mana_player = str(Player_Main1.mana)
        self.skin = Player_Main1.skin
        self.monster_name = Gros_nounours.name
        self.monster_health = str(Gros_nounours.health)
        self.skin_monster = Gros_nounours.skin
        self.text_monster.text = "Que voulez-vous faire ?"

        # mettre à jour les widgets
        self.remove_widget(self.ids.button_yes_monster)
        self.remove_widget(self.ids.button_no_monster)
        self.choice_action.pos =0, 200

        with self.canvas: #Skin player
            Rectangle(source=self.skin, pos=(300,0), size=(450, 450))
        
        with self.canvas: #Skin monster
            Rectangle(source=self.skin_monster,pos=(1200,0), size=(500, 500))

    def monster_turn(self, *args):
        self.text_monster.text ="Le monstre attaque !"
        Player_Main1.health = Player_Main1.health - Gros_nounours.attack
        self.health_player = str(Player_Main1.health)
        self.attack_system()


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
        return sm
        
if __name__ == "__main__":
    Myapp().run()