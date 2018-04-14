import chordProgressionGenerator
import midi_parser
from music_abstract import MTime
from midi_parser import MIDIParser
import midi
from music_abstract import Scale
import hashlib
import miditoaudio
import sys


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
	#printf pattern
	return pattern

def main() :
	text = "some random sad text"
	sentiment = -0.7
	if len(sys.argv) == 3 :
		var = sys.argv
		text = var[1]
		sentiment = float(var[2])
	song = createSong(text, sentiment)
	midi.write_midifile("song.mid", song)
	#miditoaudio.to_audio(sf2 = "VintageDreamsWavesv2.sf2", midi_file = "song.mid", out_dir = "")

if __name__ == "__main__":
    main()
