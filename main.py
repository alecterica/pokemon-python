# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 01:09:01 2022

@author: alexb
"""

import pygame
import config
import player_new
from game import Game
from game_state import GameState

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(config.BLACK)
pygame.display.set_caption("Pokemon Python")

clock = pygame.time.Clock()
game = Game(screen)
game.set_up()

P1 = player_new.Trainer(500, 500, 1)

while game.game_state == GameState.RUNNING:
    clock.tick(50)
    game.update()

    P1.draw(screen)
    pygame.display.flip()

