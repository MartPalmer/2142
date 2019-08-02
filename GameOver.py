#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mjpal
#
# Created:     20/07/2019
# Copyright:   (c) mjpal 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame

class GameOver(pygame.sprite.Sprite):
    speed = 10

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Game Over.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
