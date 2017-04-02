from miditime.miditime import MIDITime

from FunctionGenerator import FunctionGenerator

function_generator = FunctionGenerator(10, 10);
fun = function_generator.generateFunction()

print(fun(2))

#gen = Generator()
#notes = gen.generate()
#fun = gen.generate_function()
#print(fun(2))
# print(notes)
#
# # Instantiate the class with a tempo (120bpm is the default) and an output file destination.
# mymidi = MIDITime(120, 'myfile.mid')
#
# start = 60
# bit = 0
# prev_note = 0
# midinotes = []
# # Create a list of notes. Each note is a list: [time, pitch, velocity, duration]
# for note in notes:
#     note_details = []
#     if prev_note < note:
#         start += 1
#     elif prev_note > note:
#         start -= 1
#     prev_note = note
#     if(start > 255):
#         start = 255
#     note_details.append(bit)
#     bit += 1
#     note_details.append(start)
#     note_details.append(127)
#     note_details.append(bit)
#
#     midinotes.append(note_details)


# Add a track with those notes
#mymidi.add_track(midinotes)

# Output the .mid file
#mymidi.save_midi()