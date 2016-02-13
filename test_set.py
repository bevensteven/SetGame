import os 
import pprint
import filecmp 
from sys import argv 
from set_challenge import FindSet 
from utils import *

pp = pprint.PrettyPrinter(indent=4)

def run_tests():
	print('RUNNING TEST')
	print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	answers = {1: (9,4),
				2: (41, 8),
				3: (1, 1),
				4: (0, 0),
				5: (10, 1)}

	def check_instance(i, instance):
		try:
			assert(answers[i] == (instance.n_sets, instance.n_largest_disjoint))
		except AssertionError:
			print('assertion!')
			print((instance.n_sets, instance.n_disjoints))
			print(i)

	for i in answers:
		print(' ')
		print('##############')
		print('Case {0}'.format(i))

		file_name = 'input/{0}'.format(i)
		f = open(file_name, 'r')
		_input = list() 
		for line in f:
			_input.append(line)
		N = int(_input[0])
		cards = _input[1:]

		fs = FindSet(N, cards)
		check_instance(i, fs)

		print('##############')

	print('END TEST')
	print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
	print(' ')


run_tests()

# fetch input file from console argument 'python test_set.py <input>'
args = argv[1:]

f_name = args[0]
f = open(f_name, 'r')

input_array = list()
# assume input valid 
for line in f:
	input_array.append(line)

N = int(input_array[0])
assert(type(N) == int)
cards = input_array[1:]

fs = FindSet(N, cards)

f_out_name = 'output/' + '_out'
f_out = open(f_out_name, 'w')

# check that every disjoint set is a multiple of 3 
for s in fs.disjoints.values():
	assert(len(s)%3 == 0)


# largest_disjoint = fs.get_largest_disjoint()
# pp.pprint(largest_disjoint)
# print(len(largest_disjoint))
# valid_sets = [s in fs.sets for s in largest_disjoint]

n_sets, n_disjoints, largest_disjoint = fs.get_results()

# check that every set in the disjoint set was a set we found
for s in largest_disjoint:
	assert(s in fs.sets)

# write to an output file 
f_out.write("{0}\n{1}".format(n_sets, n_disjoints))
for _set in largest_disjoint:
	a, b, c = _set 
	a = str(transform_tuple_to_original(a))
	b = str(transform_tuple_to_original(b))
	c = str(transform_tuple_to_original(c))

	f_out.write("\n\n{0}\n{1}\n{2}".format(a, b, c))

f.close()
f_out.close()