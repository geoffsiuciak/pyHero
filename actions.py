#
# ACTIONS
#
import pygame
import xlrd
import xlsxwriter
import os
import json
import time
import data
from note import Note


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# PREPARE ALL IMAGE/AUDIO FILES
def loadAssets():
    # data.LOAD_TEXT = pygame.image.load(data.LOAD_SCREEN_TEXT).convert_alpha()
    for image in range(0, len(data.NOTES_PNG)):
        data.NOTES_PNG[image] = \
            pygame.transform.scale(
                pygame.image.load(data.NOTES_PNG[image]).convert_alpha(),
                data.NOTE_DIMENSIONS)

    data.MISSED_NOTE = \
        pygame.transform.scale(
            pygame.image.load(data.MISSED_NOTE).convert_alpha(),
            data.NOTE_DIMENSIONS)

    data.HIT_ENTER_TEXT = \
        pygame.transform.scale(
            pygame.image.load(data.HIT_ENTER_TEXT).convert_alpha(),
            data.HIT_ENTER_DIM)

    data.NOTES_BUBBLE_FX = pygame.mixer.Sound(data.NOTES_BUBBLE_FX)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# PARSE JSON, WRITE TO EXCEL FILE
def parseJson():
    new_json = 'PATH_TO_NEW_JSON_HERE.TXT'

    notes_inMidi = []
    with open(new_json) as json_file:
        json_data = json.load(json_file)

        # PULSE PER QUARTER NOTE
        PPQ = json_data['header']['ppq']

        # GET ALL NOTE ATTRIBUTES
        all_notes = json_data['tracks'][0]['notes']

        for note in range(0, len(all_notes)):
            time_ms = int(all_notes[note]['time'] * 1000)
            duration = int(all_notes[note]['duration'] * 1000)
            midi = all_notes[note]['midi']
            _note_ = [midi, duration, time_ms]
            notes_inMidi.append(_note_)

        excel_sheet = []

        for index, note in enumerate(notes_inMidi):
            excel_row = []
            if index < len(notes_inMidi) - 2:
                if notes_inMidi[index][2] == notes_inMidi[index + 1][2]:
                    midi_type = [notes_inMidi[index][0], notes_inMidi[index + 1][0]]
                    excel_row.append(getType(midi_type))
                    excel_row.append(notes_inMidi[index][1])
                    excel_row.append(notes_inMidi[index][2])
                    excel_sheet.append(excel_row)
                else:
                    midi_type = [notes_inMidi[index][0]]
                    excel_row.append(getType(midi_type))
                    excel_row.append(notes_inMidi[index][1])
                    excel_row.append(notes_inMidi[index][2])
                    excel_sheet.append(excel_row)

    new_excel = xlsxwriter.Workbook('SONG_FILES/LOADED_SONGS/Exposed_demo.xlsx')
    worksheet = new_excel.add_worksheet()

    for row, row_list in enumerate(excel_sheet):
        if row_list[1] < 615:
            row_list[1] = 0
        cell1 = str(row_list[0])
        cell2 = str(row_list[1])
        cell3 = int(row_list[2])
        worksheet.write(row, 0, cell1)
        worksheet.write(row, 1, cell2)
        worksheet.write(row, 2, cell3)
    new_excel.close()


def getType(midi_inNote):
    note_type = [0, 0, 0, 0, 0]
    if 64 in midi_inNote:
        note_type[0] = 1
    if 63 in midi_inNote:
        note_type[1] = 1
    if 62 in midi_inNote:
        note_type[2] = 1
    if 61 in midi_inNote:
        note_type[3] = 1
    if 60 in midi_inNote:
        note_type[4] = 1
    return note_type


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# READ SELECTED SONG DATA INTO NOTE OBJECT LIST
def MIDItoList(song):  # ADD SONG_PATH AS ARG RETURNED BY menuScreen()
    # READ EXCEL
    song_file = xlrd.open_workbook(song[0])
    song_data = song_file.sheet_by_index(0)
    note_count = song_data.nrows - 1

    # CREATING EMPTY LISTS
    NOTES = []
    notes_onScreen = []
    missed_notes = []
    sustain_bars = []

    # APPEND EACH CELL INTO n=3 LIST,
    # INSTANTIATE & APPEND NOTE OBJECT WITH LIST ARG
    for row in range(0, note_count):
        current_note_data = []
        for column in range(0, 3):
            if column is 0:
                note_value = song_data.cell(row, column).value.split(',')
                for i in range(len(note_value)):
                    note_value[i] = int(note_value[i])
                current_note_data.append(note_value)
            elif column > 0:
                current_note_data.append(song_data.cell(row, column).value)
        # GENERATE NOTE OBJECT FROM current_note_data,
        # APPEND TO NOTES LIST
        new_note = Note(current_note_data)
        NOTES.append(new_note)

    return NOTES, notes_onScreen, missed_notes, sustain_bars


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# DISPLAY START SCREEN
def drawStartScreen(SCREEN):
    SCREEN.blit(data.BACKGROUND, (0, 0))
    SCREEN.blit(data.LOAD_SCREEN_TEXT, data.LOAD_SCREEN_TEXT_ANCHOR)
    SCREEN.blit(data.HIT_ENTER_TEXT, data.HIT_ENTER_TEXT_ANCHOR)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# DISPLAY MENU SCREEN
def drawMenuScreen(SCREEN):
    SCREEN.blit(data.BACKGROUND, (0, 0))

    TITLE_FONT = pygame.font.SysFont(None, 75)
    TRACK_FONT = pygame.font.SysFont(None, 30)

    # to-do: make these iterable, save anchor points in data.py
    title = TITLE_FONT.render("TRACKLIST", True, (255, 255, 255))
    song1 = TRACK_FONT.render("1. " + data.SONG_1[2], True, (255, 255, 255))
    song2 = TRACK_FONT.render("2. " + data.SONG_2[2], True, (255, 255, 255))

    SCREEN.blit(title, (350, 50))
    SCREEN.blit(song1, (250, 200))
    SCREEN.blit(song2, (250, 225))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ANIMATE STATIC NOTES ONTO PLAY SCREEN
def engageAssets(SCREEN):
    SCREEN.blit(data.BACKGROUND, (0, 0))
    for png in range(0, data.BUTTON_TOTAL):
        SCREEN.blit(data.NOTES_PNG[png], data.NOTES_XY_ANCHORS[png])
        updateSCREEN()
        time.sleep(.1)

    for LANE_LINE in range(0, data.LANE_LINE_TOTAL):
        pygame.draw.line(SCREEN,
                         data.LANE_LINE_COLOR,
                         data.LANE_LINE_START_POS[LANE_LINE],
                         data.LANE_LINE_END_POS[LANE_LINE])
        updateSCREEN()
        time.sleep(.1)

    data.NOTES_BUBBLE_FX.play()


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
# DETERMINE AUDIO/NOTE SYNC VARIABLES
def startAudio(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.set_volume(0.5)
    # time.sleep(2)
    pygame.mixer.music.play(0)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# UPDATE ALL SCREEN ELEMENTS
def updateSCREEN():
    pygame.display.flip()
    pygame.display.update()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# READ INPUTS
# ANIMATE BUTTON PUSHING
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
            pygame.quit()
            exit()

    return inputs


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# PROCESS POINTS IF HIT
def hitPoints(note, notes_onScreen, game_stats):
    game_stats.total_hit += 1
    game_stats.streak += 1
    game_stats.combo = True

    notes_in_obj_HIT = 0
    for index, note_type in enumerate(note.NOTE_TYPE):  # THIS ARG = (n,n,n,n,n) 0s and 1s
        if int(note_type) == 1:
            notes_in_obj_HIT += 1
    if notes_in_obj_HIT == 1:
        game_stats.score += data.POINTS_PER_NOTE
    elif notes_in_obj_HIT > 1:
        game_stats.score += data.POINTS_PER_CHORD

    notes_onScreen.pop(0)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MISSED NOTE
def missedNoted(notes_onScreen, game_stats, missed_notes):
    game_stats.streak = 0
    game_stats.combo = False
    game_stats.recordStreak()
    missed_notes.append(notes_onScreen.pop(0))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# CHECK FOR CORRECT INPUT(S) WHILE NOTES[0] IS IN TARGET AREA
def checkForHit(notes_onScreen, inputs, game_stats, missed_notes):
    if len(notes_onScreen) > 0:
        note = notes_onScreen[0]
        if note is not None:
            if data.HIT_AREA[0] <= note.Y_POS <= data.HIT_AREA[1]:
                if inputs == note.NOTE_TYPE:
                    hitPoints(notes_onScreen[0], notes_onScreen, game_stats)
            elif note.Y_POS > data.HIT_AREA[1]:
                missedNoted(notes_onScreen, game_stats, missed_notes)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MOVE NOTE TO notes_onScreen LIST WHEN TIME
def swapToScreen(NOTES, notes_onScreen, sustain_bars):
    if NOTES:
        current_time = pygame.mixer.music.get_pos()
        note = NOTES[0]
        note_time = note.TIME_STAMP
        if note_time - data.SET_BACK_TIME <= current_time:
            note = NOTES.pop(0)
            notes_onScreen.append(note)
            # CREATE SUSTAIN BAR IF LENGTH NOT ZERO
            # BY DEFAULT 1/4 AND BELOW ARE 0
            if int(note.SUSTAIN_LENGTH) > 0:
                sustain_bars.append(note)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# UPDATE MOVING NOTES (notes_onScreen LIST)
def drawMovingNotes(SCREEN, notes_onScreen):
    for note in notes_onScreen:
        if note is not None:
            image_index_list = note.getAnchors()
            for index in image_index_list:
                SCREEN.blit(data.NOTES_PNG[index],
                            (data.MOVING_NOTE_ANCHORS[index], note.Y_POS))
            note.Y_POS += data.VELOCITY


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# UPDATE MISSED NOTES (notes_onScreen LIST)
def drawSusBars(SCREEN, sustain_bars):
    pass


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# UPDATE MISSED NOTES (notes_onScreen LIST)
def drawMissedNotes(SCREEN, missed_notes):
    if missed_notes:
        for index, note in enumerate(missed_notes):
            if note.Y_POS > 1050:
                missed_notes.pop(index)
            else:
                images = note.getAnchors()
                for index_ in images:
                    SCREEN.blit(data.MISSED_NOTE, (data.MOVING_NOTE_ANCHORS[index_], note.Y_POS))
            note.Y_POS += data.VELOCITY


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# DRAW ALL game_stats TEXT TO SCREEN
def drawText(SCREEN, game_stats):
    font = pygame.font.SysFont(None, 32)

    score = game_stats.score
    notes_hit = game_stats.total_hit
    streak = game_stats.streak
    # high_streak = game_stats.high_streak

    score_text = font.render("SCORE: " + str(score), True, data.TEXT_WHITE)
    hit_text = font.render("HIT: " + str(notes_hit), True, data.TEXT_WHITE)
    # high_streak_text = font.render("BEST: " + str(high_streak), True, data.TEXT_WHITE)

    if game_stats.combo is False:
        streak_text = font.render("STREAK: " + str(streak), True, data.TEXT_RED)
    else:
        streak_text = font.render("STREAK: " + str(streak), True, data.TEXT_GREEN)

    SCREEN.blit(score_text, (825, 25))
    SCREEN.blit(hit_text, (825, 50))

    SCREEN.blit(streak_text, (825, 100))
    # SCREEN.blit(high_streak_text, (825, 125))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# MOVE ON-SCREEN NOTES TO NEW LIST
# CHECK FOR HIT/MISS WHEN NOTES ARE IN TARGET AREA
# UPDATE POSITION OF VISIBLE NOTES
#
def noteEngine(SCREEN,
               NOTES,
               notes_onScreen,
               inputs,
               game_stats,
               missed_notes,
               sustain_bars):
    swapToScreen(NOTES, notes_onScreen, sustain_bars)
    checkForHit(notes_onScreen, inputs, game_stats, missed_notes)
    drawMovingNotes(SCREEN, notes_onScreen)
    drawMissedNotes(SCREEN, missed_notes)
    drawText(SCREEN, game_stats)
