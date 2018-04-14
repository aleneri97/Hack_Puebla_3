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
def createProgression(scale) :
	chords = [0,0,0,0]
	chords[0] = Chord(1, scale)
	lastChord = 1
	for i in range(3):
		idx = random.randint(1, len(majorProgression[lastChord - 1]))
		lastChord = majorProgression[lastChord - 1][idx - 1]
		chords[i + 1] = Chord(lastChord, scale)
	return chords

def main() :
	pass

if __name__ == "__main__":
    main()
