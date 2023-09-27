#replace max value in LL with given value

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


	def replace_max1(self,value):  #myself
		temp=self.head
		curr=self.head.next
		maxi=self.head.data
		while curr!=None:
			if maxi<curr.data:
				maxi=curr.data
				temp=curr
			curr=curr.next
		temp.data=value
		return

	def replace_max2(self,value):  #campusx
		temp=self.head
		maxi=temp

		while temp!=None:
			if temp.data>maxi.data:
				maxi=temp
			temp=temp.next

		maxi.data=value

L=Linkedlist()
L.append(101)
L.append(2)
L.append(13)
L.append(4)
L.append(5)
print(L)

L.replace_max2(15)
print(L)