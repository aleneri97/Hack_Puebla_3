import chordProgressionGenerator
import midi_parser
from music_abstract import MTime
from midi_parser import MIDIParser
import midi
from music_abstract import Scale


chords = chordProgressionGenerator.createProgression(Scale(0, "MAJORSCALE"))
pattern = midi.Pattern()
track = midi.Track()
pattern.append(track)
start = MTime()
for chord in chords:
	MIDIParser.chordToMIDI(chord, start, track)
	start.beat += 4

eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)
print pattern
midi.write_midifile("example.mid", pattern)
