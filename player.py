# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 01:57:38 2022

@author: alexb
"""
import pygame
import config
import spritesheet

# Character Sprite
sprite_sheet_image = pygame.image.load("images/N_Sprite_Sheet.png")
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

class Player:
    def __init__(self, x_position, y_position):
        print("player created")
        self.position = [x_position, y_position]
        self.image = sprite_sheet.get_image(0, 32, 32, 1, config.WHITE)
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, 10)


    def update(self):
        print("player updated")
        
    def render(self, screen):
        screen.blit(self.image, self.rect)

    def update_position(self, delta_x, delta_y):
        self.position[0] += delta_x
        self.position[1] += delta_y
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, 10)
