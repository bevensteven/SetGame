import sys
import os 
# use combinations function to perform 'n_cards choose 3 cards' with cards 
from itertools import combinations
from utils import * 


class FindSet(object):
	'''
	Takes in as input:
	- N = number of cards 
	- deck = a list of the input card strings, i.e. ['blue # \n', 'green $ \n', 'yellow @ \n']
	and displays results in format of output given by instructions.
	'''
	def __init__(self, n, deck):
		self.n = n
		self.cards = transform_deck(deck)
		self.n_sets = 0
		self.n_disjoints = 0
		self.n_largest_disjoint = 0
		self.sets = list()
		self.disjoints = dict()
		self.largest_disjoint = list()
		self.compute_results()											# compute values, print results in format of given output in instructions

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
		'''
		We can find sets given the cards by checking if every possible combination of 3 cards (N choose 3) forms a set. 
		- For every set we find, we add it to our container of sets and return it. 
		- Inside this function we also call add_disjoints to find all possible disjoint sets for later use when we want to know the largest disjoint "set of sets."
		'''
		combos = combinations(self.cards, 3) 						# all possible 3 card combinations from given cards 
		for combination in combos:
			a, b, c = combination
			if FindSet.compare_cards(a, b, c):
				self.n_sets += 1
				self.sets.append(combination)
				self.add_disjoints(combination)
		# print("Number of sets found: ", self.n_sets)
		return self.sets 

	def add_disjoints(self, combination):
		'''
		Adds disjoint set(s) to our container of disjoint sets given a particular valid set (<arg> caombination).
		- We ultimately find every possible combination of disjoint sets given the valid sets found.
		'''
		a, b, c = combination 
		dict_update = dict() 										# need to make an update dictionary since we can't add to dictionary in loop 
		for i in self.disjoints:
			curr_set = self.disjoints[i]							# check to see if we can form a disjoint set with the current set of sets
			if a not in curr_set and b not in curr_set and c not in curr_set:
				self.n_disjoints += 1
				dict_update[self.n_disjoints] = curr_set + [a, b, c]
				# print(dict_update[self.n_disjoints])
		self.n_disjoints += 1
		dict_update[self.n_disjoints] = [a, b, c]			
		self.disjoints.update(dict_update)							# update the dictionary with our new disjoint sets 

	def set_largest_disjoint(self):
		try:
			key_func = lambda x: len(self.disjoints[x])					# returns the length of a list as a heuristic 
			max_index = max(self.disjoints, key=key_func)				# figure out where the largest disjoint set is using the key function
			dset = self.disjoints[max_index]							# get the set of cards of the largest disjoint set 
			triplets = transform_list_to_triplet(dset)					# transform the set of cards back to a "set of sets" - using the fact that things should be in order in a list
			self.largest_disjoint = triplets
		except ValueError:
			# self.disjoints is empty
			return


	def get_all_sets(self):
		return self.sets

	def get_all_disjoints(self):
		return list(self.disjoints.values())

	def get_largest_disjoint(self):
		return self.largest_disjoint

	def compute(self):
		'''
		Compute all possible sets and disjoint sets. Sets values to:
		- self.n_sets
		- self.n_disjoints
		- self.disjoints
		- self.largest_disjoint
		- self.sets
		'''
		self.clean()
		self.find_sets()
		self.set_largest_disjoint()
		self.n_largest_disjoint = len(self.largest_disjoint)

	def clean(self):
		'''Reset relevant values before attempting to compute something again'''
		self.n_sets = 0
		self.n_disjoints = 0
		self.n_largest_disjoint = 0
		self.sets = list()
		self.disjoints = dict()
		self.largest_disjoint = list()

	def compute_results(self):
		'''Compute relevant values and print them to the console.'''
		self.compute()
		print(self.n_sets)
		print(self.n_largest_disjoint)

		for _set in self.largest_disjoint:
			a, b, c = _set 
			a = str(transform_tuple_to_original(a))
			b = str(transform_tuple_to_original(b))
			c = str(transform_tuple_to_original(c))
			print("\n{0}\n{1}\n{2}".format(a, b, c))

	def get_results(self):
		'''Return relevant data in tuple (<n_sets>, <n_largest_disjoint>, <largest_disjoint>)'''
		return (self.n_sets, self.n_largest_disjoint, self.largest_disjoint)
