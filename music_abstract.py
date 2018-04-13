class Scale(object):
	"""docstring for Scale."""
	def __init__(self, scaleType):
		super(Scale, self).__init__()
		self.tones = [0,0,0,0,0,0,0]
		self.intervals = [0,0,0,0,0,0,0]
		if scaleType == "MAJORSCALE" :
			self.tones = [1,3,5,6,8,10,12]
			self.intervals = [2,2,1,2,2,2,1]
		if scaleType == "MINORSCALE" :
			self.tones = [1,3,4,6,8,9,11]
			self.intervals = [2,1,2,2,1,2,2]

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
		self.tones[0] = chordTone
