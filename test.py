import chordProgressionGenerator
import midi_parser
from music_abstract import MTime
from midi_parser import MIDIParser
import midi
from music_abstract import Scale


chords = chordProgressionGenerator.createProgression(Scale(2, "MAJORSCALE"))
melody = chordProgressionGenerator.createMelody(Scale(2, "MAJORSCALE"), chords)
pattern = midi.Pattern()
chordsTrack = midi.Track()
melodyTrack = midi.Track()
pattern.append(chordsTrack)
pattern.append(melodyTrack)
start = MTime()
for chord in chords:
	MIDIParser.arpeggiator(chord, start, chordsTrack)
	start.beat += 4
MIDIParser.melodyToMIDI(melody, melodyTrack)
eot = midi.EndOfTrackEvent(tick=1)
chordsTrack.append(eot)
print pattern
midi.write_midifile("example.mid", pattern)
