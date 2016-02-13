'''
This file contains all utility functions we use to manipulate our data for ease of use.
'''

''' Constructed a symbol map for easy translation. '''
sym_map = {0: ['@', 'a', 'A'],
			1: ['$', 's', 'S'],
			2: ['#', 'h', 'H']}

def transform_tuple_to_original(tup):
	'''
	format of tup is (<color>, <symbol>, <number of symbols>, <symbol case>)
	format of original is "<color> <symbols>"
	'''
	color, sym, num_syms, case_sym = tup
	symbols = sym_map[sym][case_sym] * num_syms
	original = "{0} {1}".format(color, symbols)
	return original

def transform_original_to_tuple(org):
	'''
	format of original is "<color> <symbols>"
	format of tup is (<color>, <symbol>, <number of symbols>, <symbol case>)
	'''
	color, symbols, _break = org.split(' ')
	num_syms = len(symbols)

	def get_sym_and_case(symbols):
		sym = symbols[0]
		for i in sym_map:
			sym_list = sym_map[i]
			if sym in sym_list:
				sym_id = i 
				case_id = sym_list.index(sym)
				return sym_id, case_id

	sym, case_sym = get_sym_and_case(symbols)
	return (color, sym, num_syms, case_sym)

def transform_deck(cards):
	card_tuples = list()
	for card in cards:
		card_tuples.append(transform_original_to_tuple(card))

	return card_tuples

def transform_list_to_triplet(arr):
	'''
	Given an array of cards, we've assumed that the cards are still in order according to the properties of lists. Now we can convert each group of three cards back into its original set found earlier. 
	'''
	assert(len(arr) % 3 == 0)						# we know that any disjoint set should be a multiple of 3 as each set contains 3 cards
	triplets = []
	for i in range(0, len(arr), 3):
		triplet = (arr[i], arr[i+1], arr[i+2])
		triplets.append(triplet)
	return triplets