import pygame
from data.background import *

pygame.init()

class Game():
    def __init__(self):
        self.size = (1200, 650)
        
        self.screen = pygame.display.set_mode(self.size)
        self.background = Background(self.size)
        
    def Draw(self):
        
        self.background.Draw(self.screen)
        
        pygame.display.update()
        
    def Loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            
        self.key = pygame.key.get_pressed()
        
        if self.key[pygame.K_ESCAPE]:
            return "quit"
        
        self.Draw()
        
while True:
    if Game().Loop() == "quit":
        break
    
pygame.quit()