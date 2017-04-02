from random import randint

from miditime.miditime import MIDITime

class SongGenerator:
    def __init__(self, file_name, song_speed, song_mode, tones_range, notes):
        self.song = MIDITime(song_speed, file_name)
        self.song_mode = song_mode
        self.tones_range = tones_range
        self.notes = notes

    def generateSong(self):
        bit = 0
        notes = []
        main_note = 60
        prev_note = 0
        for note in self.notes:
            note_details = []

            note_details.append(bit)
            bit += 1

            main_note = self.generateSingleNote(self.song_mode, note, prev_note, main_note)
            note_details.append(main_note)
            prev_note = note

            note_details.append(127)
            note_details.append(randint(0, 10))

            notes.append(note_details)

        self.song.add_track(notes)
        self.song.save_midi()

    def generateSingleNote(self, mode, current_note, prev_note, main_note):
        start_note = 60
        if mode == 0:
            return current_note % (self.tones_range*2) + (start_note-self.tones_range)
        else:
            if (prev_note > current_note > (start_note-self.tones_range)) :
                return main_note - 1
            elif (prev_note < current_note < (start_note + self.tones_range)):
                return main_note + 1
            return main_note
