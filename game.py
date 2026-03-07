# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 01:52:00 2022

@author: alexb
"""
import pygame
import config

from player import Player
from game_state import GameState
import spritesheet

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
    
    def set_up(self):
        player = Player(1,1)
        self.player = player
        self.objects.append(player)
        print("Do set up")
        self.game_state = GameState.RUNNING
        
    def update(self):
        self.screen.fill(config.BLACK)
        self.handle_events()
        for object in self.objects:
            object.render(self.screen)
            
        print("update")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_w or event.key == pygame.K_UP: #up
                    self.player.update_position(0,-1)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:  # down
                    self.player.update_position(0, 1)
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:  # left
                    self.player.update_position(-1, 0)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:  # right
                    self.player.update_position(1, 0)
