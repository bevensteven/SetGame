import sys
import os 
# use combinations function to perform 'n_cards choose 3 cards' with cards 
from itertools import combinations
import disjoints

class FindSet(object):

	def __init__(self, n, deck):
		self.n = n
		self.cards = FindSet.transform_deck(deck)
		self.n_sets = 0
		self.n_disjoints = 0
		self.sets = list()
		self.disjoints = list()

	@staticmethod
	def transform_deck(cards):
		''' 
		Transform input cards into 4 element tuples for easy comparison. Formatted as:
		(<color>, <symbol>, <number of symbols>, <symbol case>)
		'''
		card_tuples = list()

		def get_sym_type(symbols):
			symbol = symbols[0]
			a = ['A', 'a', '@']				# id as 0
			s = ['S', 's', '$']				# id as 1
			h = ['H', 'h', '#']				# id as 2
			list_types = [a, s, h]
			for i, _type in enumerate(list_types):
				if symbol in _type:
					return i

		def get_case(symbols):
			character = symbols[0]
			if not character.isalpha():				# return 0 if symbol case
				return 0					
			elif character.islower():				# return 1 if lower case
				return 1
			elif character.isupper():				# return 2 if upper case 
				return 2 
			else:
				raise Exception('Undefined case')

		for card in cards:
			# each card is represented as a string "<color> <symbols>"
			print(card.split(' '))
			color, symbols, useless = card.split(' ')

			sym = get_sym_type(symbols)
			num_syms = len(symbols)
			case_sym = get_case(symbols)

			card_tuples.append( (color, sym, num_syms, case_sym) )


		return card_tuples

	@staticmethod
	def compare_cards(a, b, c):
		''' 
		Checks if the input of three cards forms a set, returning True if cards form a set, False otherwise.

		Go through every attribute of the three cards and take the set of the current attribute. We know that a set is formed when the attributes are all the same or different. Thus we can use set cardinality to see if the attributes are all the same or different:
				| attribute set | = 1 --> all attributes are the same 
				| attribute set | = 3 --> all attributes are different 
				| attribute set | = 2 --> 2 attributes are the same and 1 is different, does not form set by definition
		'''
		for i in range(4):
			att_set = set([a[i], b[i], c[i]])
			if len(att_set) == 2:	
				return False 
		return True 

	def find_sets(self):
		combos = combinations(self.cards, 3)
		for combination in combos:
			a, b, c = combination
			if FindSet.compare_cards(a, b, c):
				self.n_sets += 1
				self.sets.append(combination)
		print("Number of sets found: ", self.n_sets)
		return self.sets 

	def find_disjoints(self):


	def get_results(self):
		return [self.n_sets, self.n_disjoints, self.sets]
