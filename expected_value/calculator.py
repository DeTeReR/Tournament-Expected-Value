import logging

from expected_value.player import Player
from expected_value.tournament import Tournament

logger = logging.getLogger(__name__)


class BreakEvenCalculator(object):
	@staticmethod
	def run(tournament):
		breakeven_ev = break_even_player = None
		for win_percent in range(100):
			player = Player(win_proportion=win_percent / 100)
			player_ev = tournament.ev_for_player(player)
			logger.info('%s\'s EV is %i for %s', player, player_ev, tournament)
			if breakeven_ev is None or abs(breakeven_ev) > abs(player_ev):
				breakeven_ev = player_ev
				break_even_player = player
		return '%s is the break even player for %s' % (break_even_player, tournament)


def main():
	logging.basicConfig()
	# MTGO League
	print(BreakEvenCalculator.run(tournament=Tournament(price=28, rounds=5, wins_to_prizes={5: 66, 4: 40, 3: 18})))
	# MTGO 8-4
	print(BreakEvenCalculator.run(
		tournament=Tournament(price=14, rounds=3, losses_for_elimination=1, wins_to_prizes={3: 32, 2: 16})))
	# MTGO 4-3-2-2
	print(BreakEvenCalculator.run(
		tournament=Tournament(price=14, rounds=3, losses_for_elimination=1, wins_to_prizes={3: 16, 2: 12, 1: 8})))


if __name__ == '__main__':
	main()
