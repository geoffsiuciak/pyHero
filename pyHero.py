import pygame
import data
import actions
from stats import Stats

# INIT PYGAME, ASSETS
pygame.init()
pygame.mixer.pre_init(44100, -16, 2, 1024)
pygame.font.init()
clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((data.WIDTH, data.HEIGHT))
pygame.display.set_caption(data.CAPTION)
actions.loadAssets()


# - - - -   - - - - - - - - - - - - - - - - - - - - - - - - -
# STARTUP SCREEN
def startScreen():
    # actions.parseJson()
    # print(pygame.font.get_fonts())
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
        if keys[pygame.K_1]:
            start_screen = False
            song = data.SONG_1
            playSong(song)
        if keys[pygame.K_2]:
            start_screen = False
            song = data.SONG_2
            playSong(song)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        actions.updateSCREEN()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# SONG PLAY THROUGH LOOP
def playSong(song):
    # LOAD NOTE OBJECTS INTO LIST
    NOTES, notes_onScreen, missed_notes, sustain_bars = actions.MIDItoList(song)
    game_stats = Stats(len(NOTES))

    playing = True
    actions.engageAssets(SCREEN)
    actions.startAudio(song[1])

    while playing:
        clock.tick(data.FPS)
        actions.drawStaticAssets(SCREEN)
        inputs = actions.getInputs(SCREEN)
        actions.noteEngine(SCREEN,
                           NOTES,
                           notes_onScreen,
                           inputs,
                           game_stats,
                           missed_notes,
                           sustain_bars)
        actions.getInputs(SCREEN)
        actions.updateSCREEN()

        # print(notes_onScreen)
        # print(NOTES)

        # print(game_stats.score)

    pygame.quit()
    game_stats.getGame()


def postGame():
    # SHOW STATS
    # RETURN TO SONG SELECT
    pass


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
#
#
# RUN GAME
startScreen()
