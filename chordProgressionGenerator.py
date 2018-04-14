import random
from music_abstract import Chord
from music_abstract import Scale
from music_abstract import MTime
import midi
majorProgression = [
	[2,3,4,5,6,7],
	[5,7],
	[4,6],
	[1,2,5],
	[1],
	[4,2],
	[1,5]
]
minorProgression = [
	[2,3,4,5,6,7],
	[5,7],
	[4,6],
	[1,5,7],
	[1,6],
	[2,4,5],
	[1]
]
def createProgression(scale, seed = None) :
	if seed is not None :
		random.seed(seed)
	chords = [0,0,0,0]
	chords[0] = Chord(0, scale)
	lastChord = 0
	for i in range(3):
		idx = random.randint(1, len(majorProgression[lastChord - 1]))
		lastChord = majorProgression[lastChord - 1][idx - 1]
		chords[i + 1] = Chord(lastChord, scale)
	return chords



def createMelody(scale, chords, seed = None) :
	if seed is not None :
		random.seed(seed)
	RYTHM = [
		[0.75, 0.75, 0.5, 0.75, 0.75, 0.5],
		[0.5,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25, 0.5,0.25,0.75],
		[0.25,0.25,0.25,0.25,0.5,0.25,0.5,0.25,0.25,0.25,0.5,0.5],
		[0.5,0.5,0.5,0.25,0.5,0.25,0.5],
		[0.5,0.25,0.5,0.75,0.5,1,0.5]
	]
	beat = 0.0
	rythm = random.choice(RYTHM)
	melody = []
	idx = 0
	direction = random.choice([-2,-1,-1,0,0,0,1,1,2])
	lastnote = random.choice([1,2,3])
	while beat < 16 :
		if beat >= 0 :
			chord = chords[0]
		if beat >= 4 :
			chord = chords[1]
		if beat >= 8 :
			chord = chords[2]
		if beat >= 12 :
			chord = chords[3]
		if int(beat) % 4 == 0 or int(beat) % 4 ==  2:
			melody.append([rythm[idx], random.choice(chord.tones)])
		else :
			melody.append([rythm[idx], chord.scale.absolute[lastnote + direction]])
			lastnote += direction
			if lastnote < 0 : lastnote =0
		direction = random.choice([-2,-1,-1,0,0,0,0,1,1,2])
		beat += rythm[idx]
		idx += 1
		idx %= len(rythm)
	maxlen = 0
	for note in melody :
		if note[0] > maxlen : maxlen = note[0]
	beat = 0.0
	for note in melody :
		if beat >= 0 :
			chord = chords[0]
		if beat >= 4 :
			chord = chords[1]
		if beat >= 8 :
			chord = chords[2]
		if beat >= 12 :
			chord = chords[3]
		if note[0] == maxlen :
			note[1] =  random.choice(chord.tones)
		beat += note[0]
	return melody

def main() :
	pass

if __name__ == "__main__":
    main()
