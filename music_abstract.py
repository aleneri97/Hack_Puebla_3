class Scale(object):
	"""docstring for Scale."""
	def __init__(self, tonic, scaleType):
		super(Scale, self).__init__()
		self.tones = [0,0,0,0,0,0,0]
		self.intervals = [0,0,0,0,0,0,0]
		if scaleType == "MAJORSCALE" :
			self.tones = [1,3,5,6,8,10,12]
			self.intervals = [2,2,1,2,2,2,1]
		if scaleType == "MINORSCALE" :
			self.tones = [1,3,4,6,8,9,11]
			self.intervals = [2,1,2,2,1,2,2]
		self.absolute = []
		last = tonic
		for i in range(12 * 5):
			self.absolute.append(last)
			last += self.intervals[i % 7]
class Song(object):
	"""docstring for Song."""

	def __init__(self, tempo, timeSignature, scaleType):
		self.temp = tempo
		self.timeSignature = timeSignature
		self.scaleType = scaleType

class Chord():
	"""docstring for Chord."""
	def __init__(self, chordTone, scale):
		self.scale = scale
		self.tones = [0,0,0]
		self.tones[0] = scale.absolute[chordTone]
		self.tones[1] = scale.absolute[chordTone + 3]
		self.tones[2] = scale.absolute[chordTone + 5]

class MTime():
	"""docstring for MTime."""

	def __init__(self, beat = None, bpm = None, mtime = None):
		self.beat = 0
		self.bpm = 120
		if beat is not None :
			self.beat = beat
		if bpm is not None :
			self.bpm = bpm
		if mtime is not None :
			self.bpm = mtime.bpm
			self.beat = mtime.beat


	def toTicks(self) :
		return (60 * 100 / self.bpm) *  (self.beat)
