class Tree:

	def __init__(self, load, root=None, left=None, right=None):
		self.load = load 
		self.parent = root 
		self.left = left 
		self.right = right 

	def __str__(self):
		return str(self.load)

j = Tree('J')
h = Tree('H')
i = Tree('I')
d = Tree('D', right=j)
e = Tree('E')
f = Tree('F')
g = Tree('G', left=h, right=i)
b = Tree('B', left=d, right=e)
c = Tree('C', left=f, right=g)
a = Tree('A', left=b, right=c)

j.parent = d 
d.parent, e.parent = b, b
b.parent, c.parent = a, a
f.parent, g.parent = c, c
h.parent, i.parent = g, g

def print_BFS(tree):
	if tree == None:
		return 
	print(tree.left, tree.right)

def print_all(tree):
	if tree == None: 
		return 
	print(tree.load)
	print_all(tree.left)
	print_all(tree.right)

def find_ancestor(tree, node_a, node_b):

	parent_a, parent_b = node_a, node_b 
	parents = [node_a, node_b] 
	while node_a.parent or node_b.parent:
		parent_a = parent_a.parent 
		parent_b = parent_b.parent
		print("p_a: ", str(parent_a), "p_b: ", str(parent_b), "parents: ", [str(p) for p in parents])
		if parent_a == parent_b:
			return str(parent_a )
		if parent_a in parents:
			return str(parent_a )
		if parent_b in parents:
			return str(parent_b )
		parents += [parent_a, parent_b]

	print("fuck")



