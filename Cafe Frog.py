import pygame as py
from sys import exit
import math



class GameEngine:
    def __init__(self):
        py.init()
    def mainMenu(self):
        Screens.mainMenu()

        
    
    
class Screens:
    def mainMenu():
        screen = py.display.set_mode((1000, 800))
        
        menuBackground = py.image.load('Backgrounds/MenuAsset_Test.png')
        py.mixer.music.load("Sounds/Music/musicAssetMenu.mp3")
        py.mixer.music.play()
        py.display.set_caption("Cafe Frog")
        clock = py.time.Clock()

        #Menu loop, keeps menu going
        run = True
        scroll = 0
        tiles = math.ceil(800 / 800) + 10
        while run:
            #checks to see if user quits
            for event in py.event.get():
                if event.type == py.QUIT:
                    run = False
            #video.draw(screen, (0, 0), force_draw=False)
            for i in range(0, tiles):
                screen.blit(menuBackground, (i * 800 + scroll, 0))
            scroll -= 2
            if abs(scroll) > 500:
                scroll = 0
            py.display.update()
            clock.tick(60)
mainMenu = GameEngine()
mainMenu.mainMenu()





        
    