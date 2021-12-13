import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.graphics import Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from random import randint
from kivy.clock import Clock
from Class_characters import Player, Monster




Builder.load_file('Main.kv')

class Main(Screen):
    list_sound = ['divers/music/dungeon-quest-ost-track2.mp3', 'divers/music/enchanted-forest.mp3',
        'divers/music/dungeon-quest-ost.mp3']
    music = SoundLoader.load(list_sound[randint(0, 2)])
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


class Info(Screen):
    pass

class Load(Screen):
    pass

class Play(Screen):
    i = 0
    List_Skin = ['Img/Player.png','Img/Player_2.png','Img/Player_3.png','Img/Player_4.png']
    remaining_points = 10
    counter_health = 0
    counter_strength = 0
    counter_defense = 0
    counter_magic = 0

    def skin_player_right(self):
        skin = self.ids.skin_perso
        if self.i <= 2:
            skin.source = self.List_Skin[self.i + 1]
            self.i += 1

    def skin_player_left(self):
        skin = self.ids.skin_perso
        if self.i > 0:
            skin.source = self.List_Skin[self.i - 1]
            self.i -= 1

    def add_health(self, *args):
        if self.remaining_points > 0:
            self.remaining_points -= 1
            self.counter_health += 1
            self.ids.counter_health.text= str(self.counter_health)
            self.ids.remaining_counter.text= str(self.remaining_points)
            print("[Terminal] : 1 point de vie ajouté.")
        return self.counter_health

    def add_strength(self, *args):
        if self.remaining_points > 0:
            self.remaining_points -= 1
            self.counter_strength += 1
            self.ids.counter_strength.text= str(self.counter_strength)
            self.ids.remaining_counter.text= str(self.remaining_points)
            print("[Terminal] : 1 point de force ajouté.")
        return self.counter_strength

    def add_defense(self, *args):
        if self.remaining_points > 0:
            self.remaining_points -= 1
            self.counter_defense += 1
            self.ids.counter_defense.text= str(self.counter_defense)
            self.ids.remaining_counter.text= str(self.remaining_points)
            print("[Terminal] : 1 point de défense ajouté.")
        return self.counter_defense

    def add_magic(self, *args):
        if self.remaining_points > 0:
            self.remaining_points -= 1
            self.counter_magic += 1
            self.ids.counter_magic.text= str(self.counter_magic)
            self.ids.remaining_counter.text= str(self.remaining_points)
            print("[Terminal] : 1 point de magie ajouté.")
        return self.counter_magic

    def restart_caract(self, *args):
        self.remaining_points = 10
        self.counter_health = 0
        self.counter_strength = 0
        self.counter_defense = 0
        self.counter_magic = 0
        self.ids.counter_health.text= str(self.counter_health)
        self.ids.counter_strength.text= str(self.counter_strength)
        self.ids.counter_defense.text= str(self.counter_defense)
        self.ids.counter_magic.text= str(self.counter_magic)
        self.ids.remaining_counter.text= str(self.remaining_points)
        print("[Terminal] : réinitialisation des points.")


    def Name(self):
        name = self.ids.name_of_player
        return name.text
    
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


    def beginning(self, widget, *args):
        LayoutGame = self.ids.LayoutGame
        self.remove_widget(LayoutGame)
        Play.print(self)


class Story(Screen):
    pass



class Myapp(App):
    title = "RPGTic - Python Game"
    def build(self):
        Window.size = (1366, 768)
        Window.fullscreen = 'auto'
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(Main(name='MainWindow'))
        sm.add_widget(Info(name='InfoWindow'))
        sm.add_widget(Load(name='LoadWindow'))
        sm.add_widget(Play(name='NewGame'))
        sm.add_widget(Story(name='StoryWindow'))
        return sm
        
if __name__ == "__main__":
    Myapp().run()