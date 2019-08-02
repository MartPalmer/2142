import pygame
import random

class Enemy(pygame.sprite.Sprite):
    speed = 5
    state = "Alive"

    def __init__(self, x):
        super().__init__()
        y = -50
        self.image = pygame.image.load("badFighter.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed = random.randint(3, 12)

    def moveDown(self):
        self.rect.centery += self.speed

    def setState(self, newState):
        self.state = newState

    def getState(self):
        return self.state
