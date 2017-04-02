import numpy as np

class NoteGenerator:
    def __init__(self, start_x, tones_amount):
        self.start_x = -start_x
        self.end_x = start_x
        self.tones_amount = tones_amount

    def generateNotes(self, function):
        notes = []
        start_note = 60
        full_range = self.end_x - self.start_x
        step = full_range/self.tones_amount

        x_list = np.arange(self.start_x, self.end_x, step)
        for x in x_list:
            notes.append(int(function(x)))
        return notes
