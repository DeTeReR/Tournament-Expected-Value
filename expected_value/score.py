class Score(object):
	def __init__(self, wins=0, losses=0):
		self._wins = wins
		self._losses = losses

	@property
	def wins(self):
		return self._wins

	@property
	def losses(self):
		return self._losses

	def __eq__(self, other):
		return self.wins == other.wins and self.losses == other.losses

	def __hash__(self):
		return hash((self.wins, self.losses))

	def add_win(self):
		return self.__class__(self.wins + 1, self.losses)

	def add_loss(self):
		return self.__class__(self.wins, self.losses + 1)

	def __repr__(self):
		return '%s(w=%s, l=%s)' % (self.__class__.__name__, self.wins, self.losses)

	@property
	def rounds_played(self):
		return self.wins + self.losses
