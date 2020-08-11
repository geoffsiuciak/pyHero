#
# GLOBAL CONSTANTS
#
import pygame


# WINDOW TITLE/CAPTION
CAPTION = "pyHero"

# WINDOW DIMENSIONS
WIDTH = 1000
HEIGHT = 800

# NOTE SIZE - PNGs SCALED TO THIS
NOTE_DIMENSIONS = (80, 45)

# ASSET COLORS
LANE_LINE_COLOR = (128, 128, 128)
BACKGROUND_COLOR = (0, 0, 0)

# PROPERTIES
RUN = True
FPS = 100
BUTTON_TOTAL = 5
LANE_LINE_TOTAL = 5
MAX_NOTES_PER_SONG = 2000
HIT_AREA = (664, 720)

# NON-ITERABLE PNG ASSETS
BACKGROUND = pygame.image.load('BACKGROUND.png')
LOAD_SCREEN_TEXT = pygame.image.load('LOAD_SCREEN_TEXT.png')
LOAD_SCREEN_TEXT_ANCHOR = (410, 353)
NOTES_BUBBLE_FX = 'AUDIO_FILES/NOTES_BUBBLE_FX.wav'

# - - -
# SONGS
# - - -
SONG_1 = 'TEST_SONG.xlsx'

# MULTIPLIER STAGES
POINTS_PER_NOTE = 25
POINTS_PER_CHORD = 50
# COMBO_MULTIPLIER = [(50, 1.25),
#                     (100, 1.5),
#                     (200, 2.0),
#                     (300, 3.0)]

# GLOBAL STATIC NOTE ANCHOR POINTS - X,Y VALUES REPRESENTING
# THE WOULD-BE NW CORNER OF EACH STATIC NOTE
# (THE PNGs ARE TRANSPARENT & CROPPED TO-PIXEL)
NOTES_XY_ANCHORS = [(300, 700),  # GREEN
                    (380, 700),  # RED
                    (460, 700),  # YELLOW
                    (540, 700),  # BLUE
                    (620, 700)]  # ORANGE

# STATIC ANCHOR POINTS - X,Y VALUES REPRESENTING
# ENDING X,Y-POS OF EACH LANE LINE
LANE_LINE_END_POS = [(340, 700),  # GREEN
                     (420, 700),  # RED
                     (500, 700),  # YELLOW
                     (580, 700),  # BLUE
                     (660, 700)]  # ORANGE

# STATIC ANCHOR POINTS - X,Y VALUES REPRESENTING
# STARTING X,Y-POS OF EACH LANE LINE
LANE_LINE_START_POS = [(340, 0),  # GREEN
                       (420, 0),  # RED
                       (500, 0),  # YELLOW
                       (580, 0),  # BLUE
                       (660, 0)]  # ORANGE

# GLOBAL DYNAMIC NOTE ANCHOR POINTS - X,Y VALUES REPRESENTING
# THE WOULD-BE NW CORNER OF ALL STATIC & MOVING NOTES
# (THE PNGs ARE TRANSPARENT & CROPPED TO-PIXEL)
DYNAMIC_NOTE_X_ANCHORS = [(300, 700),  # GREEN
                          (380, 700),  # RED
                          (460, 700),  # YELLOW
                          (540, 700),  # BLUE
                          (620, 700)]  # ORANGE

# "COLOR_pushed.png" ANCHORS GIVEN UNIQUE X &or Y DIMENSIONS
# -- ORIGIN @ NW CORNER --
PUSHED_NOTES_XY_ANCHORS = [(300, 700),  # GREEN
                           (380, 700),  # RED
                           (460, 700),  # YELLOW
                           (540, 700),  # BLUE
                           (620, 700)]  # ORANGE

# STRING LIST OF COLOR NAMES
# USED TO LOOP AND GENERATE NOTE OBJECTS
NOTE_COLORS = ['GREEN',
               'RED',
               'YELLOW',
               'BLUE',
               'ORANGE',
               'GREEN_DOWN',
               'RED_DOWN',
               'YELLOW_DOWN',
               'BLUE_DOWN',
               'ORANGE_DOWN']

# STRING LIST OF COLOR NAMES
# USED TO LOOP AND GENERATE NOTE OBJECTS
NOTES_PNG = ['GREEN.png',
             'RED.png',
             'YELLOW.png',
             'BLUE.png',
             'ORANGE.png',
             'GREEN_DOWN.png',
             'RED_DOWN.png',
             'YELLOW_DOWN.png',
             'BLUE_DOWN.png',
             'ORANGE_DOWN.png']

# TO-DO:
# - ADD "SELECT IMAGE DIRECTORY" OPTION
# - AUTO READ FILE NAMES INTO ABOVE LIST(S)
# - RETURN LIST OF POINTERS TO PNGs
#
# NOTE PNG DIRECTORY & NAME LIST
IMAGE_FILE_DIRECTORY = 'IMAGE_FILES'
