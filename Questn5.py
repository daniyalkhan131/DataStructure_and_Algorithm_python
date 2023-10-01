#reversing a string using stack
class Node:
	def __init__(self,value):
		self.data=value
		self.next=None

class Stack:
	def __init__(self):
		self.top=None
	
	def isempty(self):
		return self.top==None 

	def push(self,value):
		new_node=Node(value)
		new_node.next=self.top
		self.top=new_node

	def traverse(self):
		temp=self.top
		while temp!=None:
			print(temp.data)
			temp=temp.next

	def pop(self):
		if self.isempty():
			return 'stack empty'
		else:
			data=self.top.data
			self.top=self.top.next
			return data


def reverse(string):
	strr=''
	S=Stack()
	for i in string:
		S.push(i)
	while not S.isempty():
		strr=strr+str(S.pop())

	return strr


print(reverse('TRANSFORMER')) 







