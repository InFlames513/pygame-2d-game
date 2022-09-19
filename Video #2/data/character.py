import pygame 

class Character():
    def __init__(self):
        self.x = 100
        self.y = 465
        
        self.status = "idle_sword"
        self.time = pygame.time.get_ticks()
        
        
        ########### Idle ###########
        
        self.idle_1 = pygame.transform.scale(pygame.image.load("data/files/character/adventurer-idle-00.png"), (200, 148))
        self.idle_2 = pygame.transform.scale(pygame.image.load("data/files/character/adventurer-idle-01.png"), (200, 148))
        self.idle_3 = pygame.transform.scale(pygame.image.load("data/files/character/adventurer-idle-02.png"), (200, 148))
        self.idle_4 = pygame.transform.scale(pygame.image.load("data/files/character/adventurer-idle-03.png"), (200, 148))
        
        self.idle_animation = 0
        self.idle_delay = 150
        
        self.idle_arr = [
            self.idle_1, # 0
            self.idle_2,  # 1
            self.idle_3, # 2
            self.idle_4  # 3
        ]
        
        
        ########### Idle Sword ###########
        
        self.idle_sword_1 = pygame.transform.scale(pygame.image.load("data/files/character/adventurer-idle-2-00.png"), (200, 148))
        self.idle_sword_2 = pygame.transform.scale(pygame.image.load("data/files/character/adventurer-idle-2-01.png"), (200, 148))
        self.idle_sword_3 = pygame.transform.scale(pygame.image.load("data/files/character/adventurer-idle-2-02.png"), (200, 148))
        self.idle_sword_4 = pygame.transform.scale(pygame.image.load("data/files/character/adventurer-idle-2-03.png"), (200, 148))
        
        self.idle_sword_animation = 0
        self.idle_sword_delay = 150
        
        self.idle_sword_arr = [
            self.idle_sword_1, # 0
            self.idle_sword_2,  # 1
            self.idle_sword_3, # 2
            self.idle_sword_4  # 3
        ]
        
    
    def Draw(self, screen):
        if self.status == "idle":
            screen.blit(self.idle_arr[self.idle_animation], (self.x, self.y))
        elif self.status == "idle_sword":
            screen.blit(self.idle_sword_arr[self.idle_sword_animation], (self.x, self.y))
        
        self.Loop()
        
    def Animation_Loop(self, animation, end_number, delay):
        if pygame.time.get_ticks() - self.time > delay:
            animation += 1
         
            if animation == end_number:
                animation = 0
            
            self.time = pygame.time.get_ticks()
            
        return animation
    
    def Loop(self):
        if self.status == "idle":
            self.idle_animation = self.Animation_Loop(self.idle_animation, len(self.idle_arr), self.idle_delay)
        if self.status == "idle_sword":
            self.idle_sword_animation = self.Animation_Loop(self.idle_sword_animation, len(self.idle_sword_arr), self.idle_sword_delay)