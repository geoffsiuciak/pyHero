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
LANE_LINE_COLOR = (45, 45, 45)
BACKGROUND_COLOR = (0, 0, 0)
TEXT_WHITE = (255, 255, 255)
TEXT_GREEN = (0, 255, 0)
TEXT_RED = (255, 0, 0)

# PROPERTIES
RUN = True
FPS = 60
VELOCITY = 10
BUTTON_TOTAL = 5
LANE_LINE_TOTAL = 5
MAX_NOTES_PER_SONG = 2000
SET_BACK_TIME = 1200
# - - - - - - - - - -
HIT_AREA = (695, 710)
# - - - - - - - - - -

# NON-ITERABLE FILES
BACKGROUND = pygame.image.load('IMAGE_FILES/BACKGROUND.png')
LOAD_SCREEN_TEXT = pygame.image.load('IMAGE_FILES/LOAD_SCREEN_TEXT.png')
HIT_ENTER_TEXT = 'IMAGE_FILES/HIT_ENTER.png'
HIT_ENTER_TEXT_ANCHOR = (450, 775)
HIT_ENTER_DIM = (100, 12)
LOAD_SCREEN_TEXT_ANCHOR = (410, 353)
NOTES_BUBBLE_FX = 'AUDIO_FILES/NOTES_BUBBLE_FX.wav'
MISSED_NOTE = 'IMAGE_FILES/MISSED_NOTE.png'

# - - -
# SONGS
# - - -
SONG_1 = ['SONG_FILES/LOADED_SONGS/Exposed_demo.xlsx',
          'SONG_FILES/MP3_FILES/Exposed_demo.mp3',
          '"Exposed" by Old Sol (demo)']
SONG_2 = ['SONG_FILES/LOADED_SONGS/Rosalyn.xlsx',
          'SONG_FILES/MP3_FILES/Rosalyn.mp3',
          '"Rosalyn" by Better Love']

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

MOVING_NOTE_ANCHORS = [300,  # GREEN
                       380,  # RED
                       460,  # YELLOW
                       540,  # BLUE
                       620]  # ORANGE

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
NOTES_PNG = ['IMAGE_FILES/GREEN.png',
             'IMAGE_FILES/RED.png',
             'IMAGE_FILES/YELLOW.png',
             'IMAGE_FILES/BLUE.png',
             'IMAGE_FILES/ORANGE.png',
             'IMAGE_FILES/GREEN_DOWN.png',
             'IMAGE_FILES/RED_DOWN.png',
             'IMAGE_FILES/YELLOW_DOWN.png',
             'IMAGE_FILES/BLUE_DOWN.png',
             'IMAGE_FILES/ORANGE_DOWN.png']

