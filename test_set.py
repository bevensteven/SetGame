import os 
import pprint
import filecmp 
from sys import argv 
from set_challenge import FindSet 
from utils import *

pp = pprint.PrettyPrinter(indent=4)

# print('n arguments', len(argv))
# print(str(argv))

args = argv[1:]
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
transformed_cards = transform_deck(cards)
a = transformed_cards[0]
b = transformed_cards[1]
c = transformed_cards[2]

# for i, tup in enumerate(transformed_cards):
# 	print(i, tup)

# assert(FindSet.compare_cards(a, b, transformed_cards[3]))
# assert(not FindSet.compare_cards(a, b, c))

fs = FindSet(N, cards)
# sets = fs.find_sets()

f_out_name = 'output/' + '_out'
f_out = open(f_out_name, 'w')

# for _set in sets:
# 	a, b, c = _set 
# 	a = str(transform_tuple_to_original(a))
# 	b = str(transform_tuple_to_original(b))
# 	c = str(transform_tuple_to_original(c))

# 	f_out.write("{0}\n{1}\n{2}\n\n".format(a, b, c))

# for s in fs.disjoints.values():
# 	assert(len(s)%3 == 0)


# largest_disjoint = fs.get_largest_disjoint()
# pp.pprint(largest_disjoint)
# print(len(largest_disjoint))
# valid_sets = [s in fs.sets for s in largest_disjoint]

n_sets, n_disjoints, largest_disjoint = fs.get_results()

for s in largest_disjoint:
	assert(s in fs.sets)

f_out.write("{0}\n{1}".format(n_sets, n_disjoints))
for _set in largest_disjoint:
	a, b, c = _set 
	a = str(transform_tuple_to_original(a))
	b = str(transform_tuple_to_original(b))
	c = str(transform_tuple_to_original(c))

	f_out.write("\n\n{0}\n{1}\n{2}".format(a, b, c))

f.close()
f_out.close()