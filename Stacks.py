#functions
#push
#pop
#peak
#isempty
#size

#made by me
class Node:
	def __init__(self,value):
		self.data=value
		self.next=None

class Stack:
	def __init__(self):
		self.top=None
		self.n=0

	def __str__(self):
		curr=self.top
		result=''
		while curr!=None:
			result=result+str(curr.data)+'->'
			curr=curr.next
		return result[:-2]

	def __len__(self):
		return self.n

	def push(self,value):
		new_node=Node(value)
		new_node.next=self.top
		self.top=new_node
		self.n+=1

	def pop(self):
		if self.n==0:
			print('stack empty')
		else:
			print(f'{self.top.data} is poped')
			self.top=self.top.next
			self.n-=1

	def peak(self):  #peak is for getting the top element not the ith
		#pos=0
		#curr=self.top

		#while curr!=None:
		#	if index>=self.n:
		#		return "out of index"
		#	if pos==index:
		#		return curr.data
		#	pos+=1
		#	curr=curr.next

		if self.n==0:
			print('stack empty')
		else:
			print(self.top.data)

	def isempty(self):
		if self.n==0:
			print('no elements in stack')
		else:
			print("not empty")



S=Stack()
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)

print(S)

S.pop()
S.pop()
print(S)

S.push(7)
S.push(8)
print(S)

S.peak()

S.isempty()

print(f'size is {len(S)}')


print('--------------------------------')
#made by campusx
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
			self.top=self.top.next

	#peak is for returning top element data
	def peak(self):
		if self.isempty():
			return 'stack empty'

		else:
			return self.top.data

	def size(self):
		curr=self.top
		count=0
		while curr!=None:
			count+=1
			curr=curr.next
		print(f'size is {count}')


S=Stack()
print(S.isempty())
S.push(1)
print(S.isempty())
S.push(2)
S.push(3)
S.push(4)
S.push(5)

S.traverse()
S.size()

S.pop()
S.pop()
print(S.peak())
S.pop()
print(S.peak())
S.pop()
print(S.peak())
S.pop()
print(S.peak())
print(S.pop())