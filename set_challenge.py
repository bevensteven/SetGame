import sys
import os 
# use combinations function to perform 'n_cards choose 3 cards' with cards 
from itertools import combinations
from utils import * 


class FindSet(object):
	
	def __init__(self, n, deck):
		self.n = n
		self.cards = transform_deck(deck)
		self.n_sets = 0
		self.n_disjoints = 0
		self.sets = list()
		self.disjoints = dict()


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
				self.add_disjoints(combination)
				print(self.disjoints)
				print(' ')
		print("Number of sets found: ", self.n_sets)
		return self.sets 

	def add_disjoints(self, combination):
		a, b, c = combination 
		dict_update = {} 
		for i in self.disjoints:
			curr_set = self.disjoints[i]
			if a not in curr_set and b not in curr_set and c not in curr_set:
				self.n_disjoints += 1
				dict_update[self.n_disjoints] = curr_set + [a, b, c]
		self.n_disjoints += 1
		dict_update[self.n_disjoints] = [a, b, c]
		self.disjoints.update(dict_update)

	def get_largest_disjoint(self):
		key_func = lambda x: len(self.disjoints[x])
		max_index = max(self.disjoints, key=key_func)
		dset = self.disjoints[max_index]	
		triplets = self.transform_list_to_triplet(dset)
		return triplets

	def transform_list_to_triplet(self, arr):
		assert(len(arr) % 3 == 0)
		triplets = []
		for i in range(len(arr)/3):
			triplet = (arr[i], arr[i+1], arr[i+2])
			# assert(triplet in self.sets)
			triplets.append(triplet)
		return triplets






	def get_results(self):
		return [self.n_sets, self.n_disjoints, self.sets]
