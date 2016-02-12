import sys
import os 
# use combinations function to perform 'n_cards choose 3 cards' with cards 
from itertools import combinations

class FindSet(object):

	

	def __init__(self, n, deck):
		self.n = n
		self.cards = FindSet.transform_deck(deck)
		self.n_sets = 0
		self.sets = list()

	@staticmethod
	def transform_deck(cards):
		''' 
		Transform input cards into 4 element tuples for easy comparison. Formatted as:
		(<color>, <symbol>, <number of symbols>, <symbol case>)
		'''
		card_tuples = list()

		def get_symbol_type(symbol):
			a = ['A', 'a', '@']				# id as 0
			s = ['S', 's', '$']				# id as 1
			h = ['H', 'h', '#']				# id as 2
			list_types = [a, s, h]
			for i, _type in enumerate(list_types):
				if symbol in _type:
					return i

		def get_case(character):
			if not character.isalpha():				# return 0 if symbol case
				return 0					
			elif character.islower():				# return 1 if lower case
				return 1
			elif character.isupper():				# return 2 if upper case 
				return 2 
			else:
				raise Exception('Undefined case')

		for card in cards:
			attributes = card.split(' ')
			color = attributes[0]
			symbol = get_symbol_type(attributes[1][0])
			num_symbols = len(attributes[1])
			case = get_case(symbol)
			card_tuples.append(tuple([color, symbol, num_symbols, case]))

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







# print('n arguments', len(sys.argv))
# print(str(sys.argv))

args = sys.argv[1:]
# print(args)
# assert(len(args) == 1, "please give an input file as argument")

f_name = args[0]
f = open(f_name, 'r')

input_array = list()
# assume input valid 
for line in f:
	input_array.append(line)

# print(input_array)
N = int(input_array[0])
assert(type(N) == int)
cards = input_array[1:]
# print(N, cards)
transformed_cards = FindSet.transform_deck(cards)
a = transformed_cards[0]
b = transformed_cards[1]
c = transformed_cards[2]

# for i, tup in enumerate(transformed_cards):
# 	print(i, tup)

assert(FindSet.compare_cards(a, b, transformed_cards[3]))
assert(not FindSet.compare_cards(a, b, c))

fs = FindSet(N, cards)
sets = fs.find_sets()

f_out_name = 'output/' + '_out'
f_out = open(f_out_name, 'w')

for _set in sets:
	a, b, c = _set 
	a = str(a)
	b = str(b)
	c = str(c)

	f_out.write("\n{0}\n {1}\n {2}\n".format(a, b, c))

f.close()
f_out.close()