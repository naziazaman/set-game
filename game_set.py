import random
from itertools import combinations

# Available colors
RED = 'red'
GREEN = 'green'
PURPLE = 'purple'

# Available shapes
DIAMOND = 'diamond'
SQUIGGLE = 'squiggle'
OVAL = 'oval'

# Available shadings
SOLID = 'solid'
EMPTY = 'empty'
STRIPED = 'striped'

# Available numbers
ONE = 'one'
TWO = 'two'
THREE = 'three'


class Card:
	"""A Card from the game having a number, a color, a shading, and a shape."""
	def __init__(self, _number, _color, _shading, _shape):
		self.color = _color
		self.shape = _shape
		self.shading = _shading
		self.number = _number

	def __repr__(self):
		return '{} {} {} {}'.format(self.number, self.color, self.shading, self.shape)


class SetGame:
	"""Implements the methods need to play the game SET."""
	def __init__(self):
		self.deck = self.generate_deck()
		self.board = self.generate_board()

	def is_set(self, c1, c2, c3):
		"""Determines whether three cards make a set."""
		colors = set([c1.color, c2.color, c3.color])
		numbers = set([c1.number, c2.number, c3.number])
		shapes = set([c1.shape, c2.shape, c3.shape])
		shades = set([c1.shading, c2.shading, c3.shading])
		pre_condition = (len(colors) == 3) and (len(numbers) == 3) and (len(shades) == 1)
		return pre_condition and (len(shapes) == 2 or len(shapes) == 3)

	def generate_board(self):
		"""Generates the initial board to start the game."""
		return self.draw_cards(12)

	def generate_deck(self):
		"""Generates the deck of cards for game."""
		cards = set()
		for c in [RED, GREEN, PURPLE]:
			for n in [ONE, TWO, THREE]:
				for sp in [DIAMOND, SQUIGGLE, OVAL]:
					for sd in [SOLID, EMPTY, STRIPED]:
						cards.add(Card(n, c, sd, sp))
		return cards

	def draw_cards(self, n):
		"""Draws n cards from the deck"""
		drawn = set(random.sample(self.deck, n))
		self.deck.difference_update(drawn)
		return drawn

	def find_set(self):
		"""Finds a set for a given 'board' of cards if there is any."""
		card_set = combinations(self.board, 3)
		for s in card_set:
			if self.is_set(s[0], s[1], s[2]):
				return s
		return None

	def remove_cards(self, cards):
		"""Removes the cards from the table."""
		for card in cards:
			self.board.remove(card)

	def deal(self):
		"""Deals cards from the deck."""
		drawn = self.draw_cards(3)
		for card in drawn:
			self.board.add(card)

	def play(self):
		"""Plays the game of SET and returs a list of valid sets"""
		valid_sets = []
		while True:
			if len(self.deck) == 0:
				break
			s = self.find_set()
			if s == None:
				self.deal()
			else:
				valid_sets.append(s)
				self.remove_cards(s)
		return valid_sets

def main():
	game = SetGame()
	print '\n'.join(str(s) for s in game.play())

if __name__ == '__main__':
	main()
