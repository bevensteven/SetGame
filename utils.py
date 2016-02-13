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