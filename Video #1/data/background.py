import pygame

class Background():
    def __init__(self, size):
        self.background_1 = pygame.transform.scale(pygame.image.load("data/files/backgrounds/day/Hills Layer 01.png"), size)
        self.background_2 = pygame.transform.scale(pygame.image.load("data/files/backgrounds/day/Hills Layer 02.png"), size)
        self.background_3 = pygame.transform.scale(pygame.image.load("data/files/backgrounds/day/Hills Layer 03.png"), size)
        self.background_4 = pygame.transform.scale(pygame.image.load("data/files/backgrounds/day/Hills Layer 04.png"), size)
        self.background_5 = pygame.transform.scale(pygame.image.load("data/files/backgrounds/day/Hills Layer 05.png"), size)
        self.background_6 = pygame.transform.scale(pygame.image.load("data/files/backgrounds/day/Hills Layer 06.png"), size)
        
        self.background_arr = [
            self.background_1,
            self.background_2,
            self.background_3,
            self.background_4,
            self.background_5,
            self.background_6
        ]
        
    def Draw(self, screen):
        for background in self.background_arr:
            screen.blit(background, (0,0))