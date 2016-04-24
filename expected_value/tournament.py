from expected_value.probability_results import ProbabilityResults
from expected_value.score import Score


class Tournament(object):
	def __init__(self, wins_to_prizes, price=0, losses_for_elimination=None, rounds=3):
		self._prizes = {Score(wins, rounds-wins): prizes for wins, prizes in wins_to_prizes.items()}
		self._price = price
		self._losses_for_elimination = rounds if losses_for_elimination is None else losses_for_elimination
		self._rounds = rounds

	def ev_for_player(self, player):
		prizes = 0
		for score, probability in self._recursive(player, Score(), 1):
			prizes += probability * self._prizes.get(score, 0)
		return prizes - self._price

	def _recursive(self, player, score, probability):
		if self._more_rounds(score):
			return self._recursive(player, score.add_win(), probability * player.win_proportion) \
			       + self._recursive(player, score.add_loss(), probability * player.loss_proportion)

		return ProbabilityResults({score: probability})

	def _more_rounds(self, score):
		return score.rounds_played < self._rounds and score.losses < self._losses_for_elimination

	def __repr__(self):
		return '%s(prizes:%s, price:%s)' % (self.__class__.__name__, self._prizes, self._price)
