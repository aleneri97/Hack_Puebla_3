import midi
from music_abstract import Chord
from music_abstract import Scale
from music_abstract import MTime
class MIDIParser():
	"""docstring for MIDIParser."""
	@staticmethod
	def arpeggiator(chord, start, track) :
		for i in range(2):
			on = midi.NoteOnEvent(tick=0, velocity=80, pitch=midi.C_4 + chord.tones[0])
			off = midi.NoteOffEvent(tick= 110, pitch=midi.C_4 + chord.tones[0])
			track.append(on)
			track.append(off)
			on = midi.NoteOnEvent(tick=0, velocity=80, pitch=midi.C_4 + chord.tones[1])
			off = midi.NoteOffEvent(tick= 110, pitch=midi.C_4 + chord.tones[1])
			track.append(on)
			track.append(off)
			on = midi.NoteOnEvent(tick=0, velocity=80, pitch=midi.C_4 + chord.tones[2])
			off = midi.NoteOffEvent(tick= 110, pitch=midi.C_4 + chord.tones[2])
			track.append(on)
			track.append(off)
			on = midi.NoteOnEvent(tick=0, velocity=80, pitch=midi.C_4 + chord.tones[1])
			off = midi.NoteOffEvent(tick= 110, pitch=midi.C_4 + chord.tones[1])
			track.append(on)
			track.append(off)
	@staticmethod
	def chordToMIDI(chord, start, track) :
		for tone in chord.tones:
			on = midi.NoteOnEvent(tick=0, velocity=80, pitch=midi.C_4 + tone)
			track.append(on)
		first = True
		for tone in chord.tones:
			#MIDIParser.noteToMIDI(tone, start, 4, track)
			off = midi.NoteOffEvent(tick= 220 * 4 if first else 0, pitch=midi.C_4 + tone)
			first = False
			track.append(off)
		return track


	@staticmethod
	def melodyToMIDI(melody, track) :
		for note in melody :
			MIDIParser.noteToMIDI(note[1] + 12 , note[0], track)

	@staticmethod
	def noteToMIDI(note, length, track) :
		on = midi.NoteOnEvent(tick=0, velocity=80, pitch=midi.C_4 + note)
		off = midi.NoteOffEvent(tick=int(length * 220), pitch=midi.C_4 + note)
		track.append(on)
		track.append(off)
