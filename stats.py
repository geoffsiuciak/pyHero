#
# REAL-TIME GAME STATS, METHODS
#


class Stats:
    def __init__(self, note_count):
        self.score = 0
        self.streak = 0
        self.total_hit = 0
        self.high_streak = 0
        self.combo = False
        self.note_count = note_count

    def getPercent(self):
        percent_score = self.total_hit / self.note_count
        return percent_score

    def recordStreak(self):
        if self.streak > self.high_streak:
            self.high_streak = self.streak
            self.streak = 0
