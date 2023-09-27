#reverse LL containing integer data
#in a same LL, cannot create a new list

class Node:
	def __init__(self,value):
		self.data=value
		self.next=None
class Linkedlist:
	def __init__(self):
		self.head=None
		self.n=0

	def append(self,value): #insert at tail
		
		new_node=Node(value)
		if self.head == None:
			#list is empty then add node simply
			self.head=new_node
			self.n=self.n+1

			return 

		curr=self.head
		while curr.next!=None:
			curr=curr.next
		curr.next=new_node
		self.n=self.n+1

	def __str__(self):

		curr=self.head

		result=''
		while curr!=None:
			result=result+str(curr.data)+'-->'
			curr=curr.next
		return result[:-3]


	def reverse(self): #i did myself, but it is wrong, check why it is wrong

		curr1=self.head
		curr2=self.head.next
		curr3=self.head.next.next

		while curr3!=None:

			curr2.next=curr1

			curr1=curr2
			curr2=curr3
			curr3=curr3.next

		self.head.next=None
		self.head=curr2

	def reverse2(self):

		prev_node=None 
		curr_node=self.head

		while curr_node!=None:

			next_node=curr_node.next
			curr_node.next=prev_node

			prev_node=curr_node
			curr_node=next_node
		self.head=prev_node

L=Linkedlist()
L.append(1)
L.append(2)
L.append(3)
L.append(4)
L.append(5)
L.append(6)
print(L)

L.reverse2()
print(L)