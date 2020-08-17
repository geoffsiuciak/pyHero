#
# --- NOTE CLASS ---
# init 1 per excel entry
#


class Note:
    def __init__(self, NOTE_DATA):  # JSON->LIST

        self.NOTE_TYPE = NOTE_DATA[0]  # 0,0,0,0,0
        self.SUSTAIN_LENGTH = NOTE_DATA[1]  # durationTicks
        self.TIME_STAMP = NOTE_DATA[2]  # ticks to ms

        # TO-DO FOR CONTROLLER SUPPORT - ADD HO/PO
        # self.is_HOPO = NOTE_DATA[1]  # TRUE IF HAMMER-ON/PULL-OFF (NO STRUM REQUIRED)

        self.Y_POS = -264
        self.MISSED_Y_POS = 736

    # RETURN LIST OF IMAGE INDICES BASED ON ARRAY IN self.NOTE_TYPE
    def getAnchors(self):
        images = []
        for index, note_type in enumerate(self.NOTE_TYPE):
            if int(note_type) == 1:
                images.append(index)
        return images
