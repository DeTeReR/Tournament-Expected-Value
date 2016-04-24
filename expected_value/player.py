class Player(object):
	def __init__(self, win_proportion):
		self._win_proportion = win_proportion

	@property
	def win_proportion(self):
		return self._win_proportion

	@property
	def loss_proportion(self):
		return 1 - self._win_proportion

	def __repr__(self):
		return '%s(%i%%)' % (self.__class__.__name__, self.win_proportion * 100)
