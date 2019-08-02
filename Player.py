import pygame

class Player(pygame.sprite.Sprite):
    speed = 10
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("goodFighter.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def moveLeft(self):
        self.rect.centerx -= self.speed

    def moveRight(self):
        self.rect.centerx += self.speed

    def moveUp(self):
        self.rect.centery -= self.speed
        
    def moveDown(self):
        self.rect.centery += self.speed

    def boost(self):
        self.speed = self.speed * 1.2
