#for herarchical data storage we use trees

class TreeNode:
	def __init__(self,data):
		self.data=data
		self.children=[]  #this will contain instance of tree node class
		self.parent=None #this will store parent of node

	def add_child(self, child):
		#we are not checking whether that child occur or not

		child.parent=self #child parent should be self
		self.children.append(child)

	def get_level(self):
		level=0
		p=self.parent
		while p!=None:
			p=p.parent
			level+=1
		return level 

	def print_tree(self):
		spaces=' '*self.get_level()*3 #by this we get proper formated view of tree
		prefix=spaces + "|---" if self.parent else ""


		print(prefix,self.data)
		#for i in self.children:
		#	print(i.data) #with this we are not getting children of children so we use
			#recursion as tree is a recursion data structure

		if self.children:
			for i in self.children:
				i.print_tree()

	def print_depth_children(self,i):

		spaces=' '*self.get_level()*3 #by this we get proper formated view of tree
		prefix=spaces + "|---" if self.parent else ""

		print(prefix,self.data)
		if self.children and i>0:
			for k in self.children:
				k.print_depth_children(i-1) 


def build_product_tree():
	root=TreeNode('Electronics')

	laptop=TreeNode('Laptop')
	laptop.add_child(TreeNode('Mac'))
	laptop.add_child(TreeNode('HP'))
	laptop.add_child(TreeNode('Dell'))

	cellphone=TreeNode('cellphone')
	cellphone.add_child(TreeNode('iphone'))
	cellphone.add_child(TreeNode('samsung'))
	cellphone.add_child(TreeNode('MI'))

	tv=TreeNode('tv')
	tv.add_child(TreeNode('LG'))
	tv.add_child(TreeNode('samsung'))
	tv.add_child(TreeNode('MI'))


	root.add_child(laptop)
	root.add_child(cellphone)
	root.add_child(tv)

	return root


root=build_product_tree()

print(root.data)
print(root.children[0].data)
print(root.children[0].parent.data)

print(root.children)

print()
root.print_tree()

print(root.children[0].children[0].get_level())

print()
root.print_depth_children(0)
root.print_depth_children(1)
