import midi
from music_abstract import Chord
from music_abstract import Scale
from music_abstract import MTime
class MIDIParser():
	"""docstring for MIDIParser."""
	@staticmethod
	def chordToMIDI(cord, start, track) :
		for tone in cord.tones:
			on = midi.NoteOnEvent(tick=0, velocity=80, pitch=midi.C_3 + tone)
			track.append(on)
		for tone in cord.tones:
			#MIDIParser.noteToMIDI(tone, start, 4, track)
			off = midi.NoteOffEvent(tick=100, pitch=midi.C_3 + tone)
			track.append(off)
		return track

	@staticmethod
	def noteToMIDI(note, start, length, track) :
		mtime = MTime(mtime = start);
		on = midi.NoteOnEvent(tick=mtime.toTicks(), velocity=80, pitch=midi.C_3 + note)
		mtime.beat += 4
		off = midi.NoteOffEvent(tick=mtime.toTicks(), pitch=midi.C_3 + note)
		track.append(on)
		track.append(off)
