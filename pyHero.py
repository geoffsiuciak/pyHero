import pygame
import pygame
import os
import random
import time

import data
import actions
from stats import Stats

# INIT PYGAME, ASSETS
pygame.init()
pygame.mixer.init()
pygame.font.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((data.WIDTH, data.HEIGHT))
pygame.display.set_caption(data.CAPTION)
actions.loadAssets()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# STARTUP SCREEN
def startScreen():
    start_screen = True

    while start_screen:

        actions.drawStartScreen(SCREEN)
        clock.tick(data.FPS)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            menuScreen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        actions.updateSCREEN()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# STARTUP SCREEN
def menuScreen():
    start_screen = True
    while start_screen:
        clock.tick(data.FPS)
        actions.drawMenuScreen(SCREEN)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            start_screen = False
            playSong(data.SONG_1)  # return from function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        actions.updateSCREEN()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# SONG PLAY THROUGH LOOP
def playSong(song):
    # LOAD NOTE OBJECTS INTO LIST
    NOTES, notes_onScreen = actions.MIDItoList(song)
    game_stats = Stats(len(NOTES))

    playing = True
    actions.engageButtons(SCREEN)
    while playing:
        clock.tick(data.FPS)
        actions.drawStaticAssets(SCREEN)
        inputs = actions.getInputs(SCREEN)
        actions.noteEngine(SCREEN, NOTES, notes_onScreen, inputs, game_stats)
        actions.updateSCREEN()
    pygame.quit()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
#
#
# RUN GAME
startScreen()
