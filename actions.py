#
# ACTION METHODS
#
import pygame
import xlrd
import time
import data
from note import Note
import stats


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# LOAD NOTE IMAGE FILES INTO ARRAY & SCALE
def loadAssets():
    # data.LOAD_TEXT = pygame.image.load(data.LOAD_SCREEN_TEXT).convert_alpha()
    for image in range(0, len(data.NOTES_PNG)):
        data.NOTES_PNG[image] = \
            pygame.transform.scale(
                pygame.image.load(data.NOTES_PNG[image]).convert_alpha(),
                data.NOTE_DIMENSIONS)

    data.NOTES_BUBBLE_FX = pygame.mixer.Sound(data.NOTES_BUBBLE_FX)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# DISPLAY START SCREEN
def drawStartScreen(SCREEN):
    SCREEN.blit(data.BACKGROUND, (0, 0))
    SCREEN.blit(data.LOAD_SCREEN_TEXT, data.LOAD_SCREEN_TEXT_ANCHOR)


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
def drawPushed(SCREEN, index):
    SCREEN.blit(data.NOTES_PNG[index],
                data.PUSHED_NOTES_XY_ANCHORS[index - data.BUTTON_TOTAL])


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ANIMATE STATIC NOTES ONTO PLAY SCREEN
def engageButtons(SCREEN):
    SCREEN.blit(data.BACKGROUND, (0, 0))
    for png in range(0, data.BUTTON_TOTAL):
        SCREEN.blit(data.NOTES_PNG[png], data.NOTES_XY_ANCHORS[png])
    data.NOTES_BUBBLE_FX.play()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# DETERMINE AUDIO/NOTE SYNC VARIABLES
def compSync(SCREEN):
    SCREEN.blit(data.BACKGROUND, (0, 0))
    for png in range(0, data.BUTTON_TOTAL):
        SCREEN.blit(data.NOTES_PNG[png], data.NOTES_XY_ANCHORS[png])
    data.NOTES_BUBBLE_FX.play()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# UPDATE ALL SCREEN ELEMENTS
def updateSCREEN():
    pygame.display.flip()
    pygame.display.update()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CHECK FOR HIT NOTE
# READ NOTES IN .pressed() LIST INTO TRUE/FALSE LIST,
# COMPARE WITH NOTE OBJECT IN HIT AREA
# PIGGYBACK TO ANIMATE BUTTON PUSHING
def getInputs(SCREEN):

    keys = pygame.key.get_pressed()
    inputs = [0] * data.BUTTON_TOTAL

    if keys[pygame.K_s]:
        drawPushed(SCREEN, 5)
        inputs[0] = 1
    if keys[pygame.K_d]:
        drawPushed(SCREEN, 6)
        inputs[1] = 1
    if keys[pygame.K_f]:
        drawPushed(SCREEN, 7)
        inputs[2] = 1
    if keys[pygame.K_g]:
        drawPushed(SCREEN, 8)
        inputs[3] = 1
    if keys[pygame.K_h]:
        drawPushed(SCREEN, 9)
        inputs[4] = 1

    for _event_ in pygame.event.get():
        if _event_.type == pygame.QUIT:
            quit()

    return inputs


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# HIT NOTE
def hitNote(NoteObj, game_stats):

    notes_hit = 0

    for _input_ in NoteObj.NOTE_TYPE:
        if _input_ == 1:
            notes_hit += 1
    if notes_hit == 1:
        game_stats.score += data.POINTS_PER_NOTE
    elif notes_hit > 1:
        game_stats.score += data.POINTS_PER_CHORD

    game_stats.streak += 1
    game_stats.combo = True
    NoteObj.delete()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MISSED NOTE
def missedNoted(NoteObj, game_stats):
    game_stats.streak = 0
    game_stats.combo = False
    game_stats.recordStreak()
    NoteObj.delete()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CHECK FOR CORRECT INPUT(S) WHILE NOTES[0] IS IN TARGET AREA
def checkForHit(NOTES, inputs, game_stats):
    if data.HIT_AREA[0] < NOTES[0].Y_POS < data.HIT_AREA[1]:
        if inputs == NOTES[0].NOTE_TYPE:
            hitNote(NOTES[0], game_stats)
        elif inputs != NOTES[0].NOTE_TYPE:
            missedNoted(NOTES[0], game_stats)
    elif NOTES[0].Y_POS > data.HIT_AREA[1]:
        missedNoted(NOTES[0], game_stats)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MOVE ON-SCREEN NOTES TO NEW LIST
# CHECK FOR HIT/MISS WHEN NOTES ARE IN TARGET AREA
#
def noteEngine(SCREEN, NOTES, notes_onScreen, inputs, game_stats):

    # WHEN IT'S TIME FOR A NOTE TO APPEAR ON SCREEN, .pop() TO notes_onScreen LIST
    for note in NOTES:
        if pygame.mixer.music.get_pos() == note.TIME_STAMP:
            notes_onScreen.append(NOTES.pop(NOTES[0]))

    # CHECK HIT/MISS
    checkForHit(NOTES, inputs, game_stats)

    # UPDATE ALL NOTES ON SCREEN
    for note in notes_onScreen:
        SCREEN.blit(NOTES[note.IMAGE], note.Y_POS)
        note.Y_POS += 2


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# READ SONG MIDI DATA INTO NOTE OBJECTS, LOAD IN GAME_NOTES_LIST
def MIDItoList(song):  # ADD SONG_PATH AS ARG RETURNED BY menuScreen()
    # READ EXCEL
    song_file = xlrd.open_workbook(song)
    song_data = song_file.sheet_by_index(0)
    note_count = song_data.nrows - 1

    # CREATING EMPTY LIST FOR NOTES AND FOR EVENTUAL NOTES ON-SCREEN
    NOTES = []
    notes_onScreen = []

    # APPEND EACH CELL INTO n=3 LIST,
    # INSTANTIATE & APPEND NOTE OBJECT WITH LIST ARG
    for note in range(1, note_count):
        current_note_args = [[int, int, int, int, int], int, int] * 3
        for cell in range(0, 2):
            current_note_args.append(song_data.cell(note, cell).value)
        NOTES.append(Note(current_note_args))

    return NOTES, notes_onScreen
