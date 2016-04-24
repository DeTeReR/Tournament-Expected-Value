from collections import defaultdict


class ProbabilityResults(object):
	def __init__(self, score_probabilities):
		self._score_probabilities = score_probabilities

	@property
	def score_probabilities(self):
		return self._score_probabilities

	def __repr__(self):
		return '%s(%s)' % (self.__class__.__name__, self.score_probabilities)

	def __add__(self, other):
		new_score_probabilities = defaultdict(lambda: 0, self._score_probabilities.items())
		for score, probability in other.score_probabilities.items():
			new_score_probabilities[score] += probability
		return self.__class__(new_score_probabilities)

	def __iter__(self):
		for score, probability in self.score_probabilities.items():
			yield score, probability

