#sum of the elements at odd position

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

	def summ_odd(self):

		curr=self.head
		index=0
		summ=0
		while curr!=None:
			if index%2==1:
				summ+=curr.data
			curr=curr.next
			index+=1
		print(summ)



L=Linkedlist()
L.append(2)
L.append(3)
L.append(4)
L.append(5)
L.append(6)
print(L)

L.summ_odd()

