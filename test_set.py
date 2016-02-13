from set_challenge import FindSet 
import filecmp 
from sys import argv 
from utils import *
import os 
import pprint


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

	f_out.write("{0}\n{1}\n{2}\n\n".format(a, b, c))

for s in fs.disjoints.values():
	assert(len(s)%3 == 0)

def check_others():
	size = len(sets)
	mappings = dict(zip(range(size), sets))
	disjoint_sets = list()
	for i in range(len(mappings)):
		pivot = i
		curr_disjoint = set()
		for item in mappings[pivot]:
			curr_disjoint.add(item)
		for j in range(len(mappings)):
			if i == j:
				continue 
			jset = set(mappings[j])

class Disjoint:

    def __init__(self):
        self.sets = []

    def createSet(self, repr):
        self.sets.append([repr])

    def mergeSets(self, repr1, repr2):
        set1 = self.findSet(repr1);
        set2 = self.findSet(repr2);
        if set1 != set2:
            set1.extend(set2);
            self.sets.remove(set2);

    def findSet(self, repr1):
        for oneSet in self.sets:
            if repr1 in oneSet:
                return oneSet


    def getSets(self):
        return self.sets

def test_simple(self):
        dis = disjoint.Disjoint();
        for i in range(1, 6):
            dis.createSet(i)
        pairs = [[1, 2], [2, 4], [4, 5]]
        for p in pairs:
            p1 = p[0];
            p2 = p[1];

            if dis.findSet(p1) != dis.findSet(p2):
                dis.mergeSets(p1, p2)

        expetctedSets = [[1, 2, 4, 5], [3]];
        self.assertEqual(expetctedSets, dis.getSets())

# def test(card_sets):
# 	dis = Disjoint()
# 	cards = set()
# 	for a, b, c in card_sets:
# 		cards.add(a)
# 		cards.add(b)
# 		cards.add(c)
# 	cards = list(cards)
# 	print(cards)
# 	for card in cards:
# 		dis.createSet(card)
# 	for c1, c2, c3 in card_sets:
largest_disjoint = fs.get_largest_disjoint()
print(largest_disjoint, len(largest_disjoint))
valid_sets = [s in fs.sets for s in largest_disjoint]

f.close()
f_out.close()