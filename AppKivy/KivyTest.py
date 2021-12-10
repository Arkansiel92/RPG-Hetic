import kivy
from kivy.uix.behaviors import button
kivy.require('2.0.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.animation import Animation
from random import randint

class Main_Player:
    def __init__(self, health, attack, defense, magic, skin):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.skin = skin 

Builder.load_file('MyTest.kv')

class Main(Screen):
    list_sound = ['divers/music/dungeon-quest-ost-track2.mp3', 'divers/music/enchanted-forest.mp3',
        'divers/music/dungeon-quest-ost.mp3']
    music = SoundLoader.load(list_sound[randint(0, 2)])
    music.loop = True
    if music:
        music.play()
    def sound(self, switchObject, switchValue):
        if switchValue:
            print("Terminal : play music")
            self.music.play()
        else:
            print("Terminal : stop music")
            self.music.stop()


class Info(Screen):
    pass

class Load(Screen):
    pass

class Play(Screen):

    def Name(self):
        name = self.ids.name_of_player
        return name.text
  
    
    def print(self, *args):

        name = Play.Name(self)
        print("Nom du joueur :", name)
        text_story = self.ids.text_story
        text_story.pos = 0, 100
        text_story.text = """
    Bienvenue {}. Ton periple debut ici !
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
        #anim = Animation(opacity=0)
        #anim.start(LayoutGame)
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