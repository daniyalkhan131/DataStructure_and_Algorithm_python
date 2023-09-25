#linked list
#it store data in non continuous memory locations
#deletion and insertion in array need O(n) while linkedlist need O(1) for write operations
#memmory wastage in array(in dynamic array also)
#linkedlist read operation need O(n) time

#if our work require read heavy operations then use arrays and if require write heavy
#operations then use linkedlist


#node is object, so we create class of node
class Node:

	def __init__(self,value):
		self.data=value
		self.next=None
a=Node(1)
b=Node(2)
c=Node(3)

a.next=b
b.next=c
print(a.next,id(b)) #same address
print(b.next,id(c))
print('---------------------------------')
print()


class Node:

	def __init__(self,value):
		self.data=value
		self.next=None

#head=None is empty linkedlist

class LinkedList:
	def __init__(self):
		#empty linkedlist
		self.head=None
		#no. of nodes in linkedlist
		self.n=0

	def __len__(self):
		return self.n

	def insert_head(self,value): #insert at front

		#new  node
		new_node=Node(value)

		#vreate connection
		new_node.next=self.head

		#reassign head
		self.head=new_node

		#increment n
		self.n=self.n+1

	def __str__(self):

		curr=self.head

		result=''
		while curr!=None:
			result=result+str(curr.data)+'-->'
			curr=curr.next
		return result[:-3]


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


	def insert_after(self,after,value):

		new_node=Node(value)

		curr=self.head
		
		#while curr.data!=after:  #this code will destry when value not present
		#	curr=curr.next           we have to write code so it can work in all senarios

		while curr!=None:
			if curr.data==after:
				break
			curr=curr.next

		#case1 break-> item apko mmil gaya and curr is not none
		#case2 loop pura chala -> item nai mila and curr = None

		if curr!=None:
			new_node.next=curr.next
			curr.next=new_node
			self.n=self.n+1
		else:
			print('item not found')


#deletion

	def delete_full(self):

		self.head=None
		self.n=0

	def delete_fromhead(self):

		if self.head==None:
			print("cannot delete LL is empty")
			return

		temp=self.head             #we dont need to do this, temp assignment and del
		self.head=self.head.next   #because python have garbage collector that do that
		temp.next=None

		del temp

		self.n=self.n-1

	def delete_fromtail(self): #pop

		if self.head==None:
			print('cannot delete LL is empty')
			return

		#we have to check for 1 node also otherwise error if 1 item in LL
		if self.head.next==None:
			self.delete_fromhead()
			return 
		curr=self.head
		while curr.next.next!=None:
			curr=curr.next
		curr.next=None

		self.n=self.n-1

	def delete_byvalue(self,value):

		if self.head==None:
			print('cannot delete LL is empty')
			return

		if self.head.data==value:
			self.head=self.head.next
			self.n=self.n-1
			return
		curr=self.head.next
		curr2=self.head

		while curr!=None:
			if curr.data==value:
				curr2.next=curr.next
				del curr
				break
			curr=curr.next
			curr2=curr2.next

		self.n=self.n-1

	def delete_byvalue2(self,value):

		if self.head==None:
			print('LL is empty')
			return
		if self.head.data==value:
			self.head=self.head.next
			self.n=self.n-1
			return

		curr=self.head
		while curr.next!=None:
			if curr.next.data==value:
				curr.next=curr.next.next
				self.n=self.n-1
				return
			curr=curr.next
		if curr.data==value:
			self.head=None
			self.n=self.n-1
		else:
			print("not in LL")

#all three are working fine but this one is best
	def delete_byvalue3(self,value):
		
		if self.head==None:
			print('LL is empty')
			return
		if self.head.data==value:
			return self.delete_fromhead()

		curr=self.head	
		while curr.next!=None:
			if curr.next.data==value:
				break
			curr=curr.next

		if curr.next==None:
			print('item not found')
		else:
			curr.next=curr.next.next
			self.n=self.n-1	

#searchin

	def search(self,item):
		curr=self.head
		index=0
		while curr!=None:
			if curr.data==item:
				print(index)
				return
			curr=curr.next
			index+=1
		print("not in LL")

#delete by index







#search by index

	def __getitem__(self,index):
		curr=self.head
		pos=0
		if self.n<=index:
			return "index out of range"
		while curr!=None:
			if pos==index:
				return curr.data
			pos+=1
			curr=curr.next


L=LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)

print(len(L))

print(L)

L.append(5)
print(L)

L.insert_after(2,10)
print(L)

L.delete_full()
print(L)
print(len(L))

L=LinkedList()
L.append('a')
L.append('b')
L.append('c')
L.append('d')
print(L)
print(len(L))

L.delete_fromhead()
print(L)
print(len(L))

L.delete_fromtail()
print(L)
print(len(L))

L.insert_head('a')
L.append('d')
L.append('e')
print(L)
print(len(L))
print("--------")


print(L)
L.delete_byvalue3('a')
print(L)
L.delete_byvalue3('e')
print(L)
L.delete_byvalue3('b')
L.delete_byvalue3('d')
L.delete_byvalue3('c')
print(L)
print(len(L))
L.delete_byvalue3('e')

print('------------------')
L.append('a')
L.append('b')
L.append('c')
L.append('d')

L.search('e')
L.search('a')

print('--------------------')
print(L[3])
print(L[4])


#array vs LL
#in array insert delete is heavy while traversing or indexing is easy(fast)
#in LL insert delete is light while is traversing or indexing is heavy(slow)
