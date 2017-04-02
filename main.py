from FunctionGenerator import FunctionGenerator
from NoteGenerator import NoteGenerator
from SongGenerator import SongGenerator



function_generator = FunctionGenerator(10, 10);
function = function_generator.generateFunction()
note_generator = NoteGenerator(1000, 100, 60)
notes = note_generator.generateNotes(function)
print(notes)

song_generator = SongGenerator("myfile.mid", 500, 0, notes)
song_generator.generateSong()
