#to implement set in python, one of the ways use is BST

#at most two child and left to node has small value and on right greater value
#duplicate element not in BST
#for searching in BST- BFS
					#- DFS- inorder
					#		preorder
					#		postorder


class BinarySearchTreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

	def add_child(self,data):
		if data==self.data:
			return

		if data<self.data:
			if self.left:
				self.left.add_child(data)
			else:
				self.left=BinarySearchTreeNode(data)

		else:
			if self.right:
				self.right.add_child(data)

			else:
				self.right=BinarySearchTreeNode(data)

	def delete(self,val):
		if val<self.data:
			if self.left:
				self.left=self.left.delete(val)
			#else: python at default return None
			#	return None

		elif val>self.data:
			if self.right:
				self.right=self.right.delete(val)

		else:
			#both child None
			if self.left is None and self.right is None:
				return None

			#one of child is None
			if self.left is None:
				return self.right

			if self.right is None:
				return self.left

			#can go with max value in left subtree
			min_val=self.right.find_min()
			self.data=min_val
			self.right=self.right.delete(min_val)

		return self


	def inorder_traversal(self):
		elements=[]

		if self.left:
			elements+=self.left.inorder_traversal()

		elements.append(self.data)

		if self.right:
			elements+=self.right.inorder_traversal()

		return elements

	def search(self,val):
		if self.data==val:
			return True

		if val<self.data:
			if self.left:
				return self.left.search(val)
			else:
				return False
		if val > self.data:
			if self.right:
				return self.right.search(val)
			else:
				return False

	#find_min(), find_max(), calculate_sum(), postorder_traversal(), preorder_traversal()

	def find_min(self):
		if self.left:
			return self.left.find_min()
		else:
			return self.data

	def find_max(self):
		if self.right:
			return self.right.find_max()
		else:
			return self.data 

	def calculate_sum(self):
		result=0
		result+=self.data
		if self.left:
			result+=self.left.calculate_sum()
		if self.right:
			result+=self.right.calculate_sum()
		return result
			
	def preorder_traversal(self):
		elements=[]

		elements.append(self.data)

		if self.left:
			elements+=self.left.preorder_traversal()

		if self.right:
			elements+=self.right.preorder_traversal()

		return elements

	def postorder_traversal(self):
		elements=[]

		if self.left:
			elements+=self.left.postorder_traversal()

		if self.right:
			elements+=self.right.postorder_traversal()

		elements.append(self.data)

		return elements

#copied from internet
def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.data))
        printTree(node.right, level + 1)


def build_tree(elements):
	root=BinarySearchTreeNode(elements[0])

	for i in range(1,len(elements)):
		root.add_child(elements[i])

	return root


nums=[6,3,9,7,1,9,1,1,9,9,2,0,3,3]
root=build_tree(nums)

print(root.inorder_traversal())
#one of the utility of BST is to sort the elements in the list
#and other utility is set type give

print(root.search(9))


countries=['india','pakistan','china','germany','usa','india','uk','usa']
root=build_tree(countries)
print(root.search('usa'))
print(root.inorder_traversal())


nums=[5,2,12,1,3,9,21,19,25]
root=build_tree(nums)

printTree(root)

print('min',root.find_min())
print('max',root.find_max())

print('sum',root.calculate_sum())

print('preorder_traversal',root.preorder_traversal())

print('preorder_traversal',root.postorder_traversal())

root.delete(12)
printTree(root)
print(root.inorder_traversal())