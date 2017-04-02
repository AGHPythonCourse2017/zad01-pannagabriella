import numpy as np

class NoteGenerator:
    def __init__(self, start_x, tones_amount, range_of_tones):
        self.start_x = -start_x
        self.end_x = start_x
        self.tones_amount = tones_amount
        self.range_of_tones = range_of_tones

    def generateNotes(self, function):
        function_results = []
        notes = []
        start_note = 60
        full_range = self.end_x - self.start_x
        step = full_range/self.tones_amount

        x_list = np.arange(self.start_x, self.end_x, step)
        for x in x_list:
            function_results.append(int(function(x)))
        for x in function_results:
            notes.append(x % (self.range_of_tones*2) + (start_note-self.range_of_tones))
        return notes
