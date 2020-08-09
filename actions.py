#
# ACTION METHODS
#
import pygame
import time
import data
import note


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# LOAD NOTE IMAGE FILES INTO ARRAY & SCALE
def loadAssets():
    # data.LOAD_TEXT = pygame.image.load(data.LOAD_SCREEN_TEXT).convert_alpha()
    for image in range(0, len(data.NOTES_PNG)):
        data.NOTES_PNG[image] = \
            pygame.transform.scale(
                pygame.image.load(data.NOTES_PNG[image]).convert_alpha(), data.NOTE_DIMENSIONS)

    data.NOTES_BUBBLE_FX = pygame.mixer.Sound(data.NOTES_BUBBLE_FX)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# DISPLAY START SCREEN
def drawStartScreen(SCREEN):
    SCREEN.blit(data.BACKGROUND, (0, 0))
    SCREEN.blit(data.LOAD_SCREEN_TEXT, data.LOAD_SCREEN_TEXT_ANCHOR)
    # START_MESSAGE = pygame.font.Font('freesansbold.ttf', 25)
    # TextSurf, TextRect = text_objects(text, largeText)
    # TextRect.center = ((display_width / 2), (display_height / 2))
    # gameDisplay.blit(TextSurf, TextRect)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# DISPLAY MENU SCREEN
def drawMenuScreen(SCREEN):
    SCREEN.blit(data.BACKGROUND, (0, 0))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# DRAW/REDRAW ALL STATIC ASSETS ON LOOP
def drawStaticAssets(SCREEN):
    SCREEN.blit(data.BACKGROUND, (0, 0))
    # LOOP TO DRAW EACH LANE LINE
    for LANE_LINE in range(0, data.LANE_LINE_TOTAL):
        pygame.draw.line(SCREEN,
                         data.LANE_LINE_COLOR,
                         data.LANE_LINE_START_POS[LANE_LINE],
                         data.LANE_LINE_END_POS[LANE_LINE])
    # LOOP TO BLIT EACH STATIC NOTE
    for png in range(0, data.BUTTON_TOTAL):
        SCREEN.blit(data.NOTES_PNG[png], data.NOTES_XY_ANCHORS[png])


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# BLIT "COLOR_PUSHED.png" ON-PUSH
# color_index = INT 0-N REPRESENTING BUTTON PUSHED
def drawPushed(SCREEN, note_index):
    SCREEN.blit(data.NOTES_PNG[note_index], data.PUSHED_NOTES_XY_ANCHORS[note_index - 5])


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ANIMATE STATIC NOTES ONTO PLAY SCREEN
def engageButtons(SCREEN):
    SCREEN.blit(data.BACKGROUND, (0, 0))
    for png in range(0, data.BUTTON_TOTAL):
        SCREEN.blit(data.NOTES_PNG[png], data.NOTES_XY_ANCHORS[png])
    data.NOTES_BUBBLE_FX.play()
    # time.sleep(1)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# UPDATE ALL SCREEN ELEMENTS
def update_screen(SCREEN):
    drawStaticAssets(SCREEN)
    pygame.display.flip()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
def readNotes(NOTES_LIST):
    for note_object in NOTES_LIST:
        while NOTES_LIST[note_object] is not None:
            pass


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ON-STRUM LOGIC
def checkForNote(self):
    pass

#
# TO-DO:
#
# SCORE COUNTER/METER?
# OTHER STATIC ASSETS
#
