import chordProgressionGenerator
import midi_parser
from music_abstract import MTime
from midi_parser import MIDIParser
import midi
from music_abstract import Scale
import hashlib

def createSong(text, sentiment) :
	h = hash(text)
	sentiment = int(sentiment * 3)
	scale = Scale(sentiment, "MAJORSCALE")
	if sentiment >= 0 :
		scale = Scale(sentiment, "MAJORSCALE")
	if sentiment < 0 :
		scale = Scale(sentiment, "MINORSCALE")
	chords = chordProgressionGenerator.createProgression(scale, h)
	melody = chordProgressionGenerator.createMelody(scale, chords, h)
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

def main() :
	text = "some random sad text"
	sentiment = -0.7
	createSong(text, sentiment)

if __name__ == "__main__":
    main()
