#follow FIFO, have front and rear pointers, insert-enqueue delete-dequeue

#implementation using Linkedlist

class Node:
	def __init__(self,value):
		self.data=value
		self.next=None
class Queue:
	def __init__(self):
		self.front=None
		self.rear=None

	def enqueue(self,value):
		new_node=Node(value)

		if self.rear==None:     #queue is empty
			self.front=new_node
			self.rear=self.front
		else:
			self.rear.next=new_node
			self.rear=new_node

	def dequeue(self):

		if self.front==None:
			return 'empty queue'
		else:
			data=self.front.data
			self.front=self.front.next
			return data

	def traverse(self):
		curr=self.front
		strr=''
		while curr!=None:
			strr+='|'+str(curr.data)
			curr=curr.next
		return strr

	def isempty(self):
		if self.front==None:
			return True
		else:
			return False

	def size(self):
		curr=self.front
		count=0
		while curr!=None:
			count+=1
			curr=curr.next
		return count

	def front_item(self): #for peeking
		if self.isempty():
			return 'empty queue'
		else:
			return self.front.data

	def rear_item(self): #for peeking
		if self.isempty():
			return 'empty queue'
		else:
			return self.rear.data


Q=Queue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
print(Q.traverse())
Q.dequeue()
print(Q.traverse())

print(Q.isempty())
print(Q.front_item())
print(Q.rear_item())

Q.dequeue()
Q.dequeue()

print(Q.isempty())
print(Q.front_item())
print(Q.rear_item())