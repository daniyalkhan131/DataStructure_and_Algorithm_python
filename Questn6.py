#text editor
#we have to do undo and redo operations
#two strings given like hello and uuur so u means undo and r means redo, we have to apply
#these in the given order to the hello string


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

def text_editor(string,ops):

	S1=Stack()
	S2=Stack()
	for i in string:
		S1.push(i)
	for i in ops:
		if i=='u':
			temp=S1.pop()
			S2.push(temp)
		elif i=='r':
			temp=S2.pop()
			S1.push(temp)

	strr=''
	while not S1.isempty():
		strr=str(S1.pop())+strr
	return strr

print(text_editor('daniyalkhan','uuuurruuuurr'))




