import pygame
import os
import random
import time

import data
import actions
import note

pygame.init()
pygame.mixer.init()
pygame.font.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((data.WIDTH, data.HEIGHT))
pygame.display.set_caption(data.CAPTION)
actions.loadAssets()
print(len(data.NOTES_PNG))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# STARTUP SCREEN
def startScreen():
    start_screen = True

    while start_screen:

        actions.drawStartScreen(SCREEN)
        clock.tick(data.FPS)

        for event in pygame.event.get():
            # GREEN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    playSong()
            #     # QUIT
            if event.type == pygame.QUIT:
                start_screen = False

        pygame.display.flip()
        pygame.display.update()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# STARTUP SCREEN
def menuScreen():
    start_screen = True

    while start_screen:

        actions.drawStartScreen(SCREEN)
        clock.tick(data.FPS)

        for event in pygame.event.get():
            # GREEN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    playSong()

        current_keys = pygame.event.get_pressed()
        if current_keys[pygame.K_RETURN]:
            playSong()

            if event.type == pygame.QUIT:
                start_screen = False

        pygame.display.flip()
        pygame.display.update()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# SONG PLAY THROUGH LOOP
def playSong():
    playing = True
    actions.engageButtons(SCREEN)
    while playing:

        # redraw WIN after each event
        actions.drawStaticAssets(SCREEN)

        clock.tick(data.FPS)

        for event in pygame.event.get():
            # GREEN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    actions.drawPushed(SCREEN, data.BUTTON_TOTAL)
            # RED
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    actions.drawPushed(SCREEN, data.BUTTON_TOTAL + 1)
            # YELLOW
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    actions.drawPushed(SCREEN, data.BUTTON_TOTAL + 2)
            # BLUE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    actions.drawPushed(SCREEN, data.BUTTON_TOTAL + 3)
            # ORANGE
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    actions.drawPushed(SCREEN, data.BUTTON_TOTAL + 4)
            # quit
            if event.type == pygame.QUIT:
                playing = False

            pygame.display.flip()
            pygame.display.update()

    pygame.quit()


startScreen()
