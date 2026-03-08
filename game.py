# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 01:52:00 2022

@author: alexb
"""
import pygame
import config
import tile

from player import Player
from game_state import GameState
import spritesheet


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE

    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        B1=tile.tile_object(112,112,1)
        self.objects.append(B1)
        # print("Do set up")
        self.game_state = GameState.RUNNING

    def update(self):
        self.screen.fill(config.BLACK)
        self.handle_events()

        try:
            self.player.update_position(self.player.movelist[-1][0], self.player.movelist[-1][1])
        except IndexError:
            pass
        for obj in self.objects:
            obj.render(self.screen)
            pygame.draw.rect(self.screen,config.WHITE,obj.rect,width=1)


        # print("update")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            elif event.type == pygame.K_ESCAPE:
                self.game_state = GameState.ENDED
            else:
                self.player.process_event(event)
