import pygame

class Bullet(pygame.sprite.Sprite):
    speed = 20
    state = "Alive"

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("bullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def moveUp(self):
        self.rect.centery = self.rect.centery - self.speed

    def setState(self, newState):
        self.state = newState

    def getState(self):
        return self.state


