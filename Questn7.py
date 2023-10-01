#Given an expression string exp, write a program to examine whether the pairs
#and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression.
#Input: exp = “[()]{}{[()()]()}” 
#Output: Balanced

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

	def peek(self):
		if self.isempty():
			return 'empty stack'
		else:
			return self.top.data


def parenthesis(string):

	S1=Stack()
	for i in string:
		if i=='[' or i=='{' or i=='(':
			S1.push(i)
			print(1)

		else:
			if i==']':
				if S1.peek()=='[':
					S1.pop()
					print(2)
				else:
					S1.push(i)
					print(3)
			elif i=='}':
				if S1.peek()=='{':
					S1.pop()
					print(4)
				else:
					S1.push(i)
					print(5)
			if i==')':
				if S1.peek()=='(':
					S1.pop()
					print(6)
				else:
					S1.push(i)
					print(7)
	if S1.isempty():
		return 'balanced'
	else:
		return 'unbalanced'


strr='[(])'
print(strr)
print(parenthesis(strr))







