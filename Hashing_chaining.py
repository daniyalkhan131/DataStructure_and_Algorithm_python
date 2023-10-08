#array of linkedlist we make

#we add functionality of rehashing it happens when load factor is more than some
#value we initialised like if on one index the LL become large so O(1) will not
#be achieved
#load factor =size/capacity


class Node:

	def __init__(self,key,value):
		self.key=key
		self.value=value
		self.next=None

#we only kept the important methods on linkedlist for our usecase
class LinkedList:
	def __init__(self):
		self.head=None
		self.n=0

	def __len__(self):
		return self.n

	def __str__(self):

		curr=self.head

		result=''
		while curr!=None:
			result=result+str(curr.data)+'-->'
			curr=curr.next
		return result[:-3]


	def append(self,key,value): #insert at tail
		
		new_node=Node(key,value)

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

#deletion
	def delete_fromhead(self):

		if self.head==None:
			print("cannot delete LL is empty")
			return

		temp=self.head
		self.head=self.head.next
		temp.next=None

		del temp

		self.n=self.n-1

	def delete_byvalue(self,key):
		
		if self.head==None:
			print('LL is empty')
			return
		if self.head.key==key:
			return self.delete_fromhead()

		curr=self.head	
		while curr.next!=None:
			if curr.next.key==key:
				break
			curr=curr.next

		if curr.next==None:
			print('item not found')
		else:
			curr.next=curr.next.next
			self.n=self.n-1	

	def traverse(self):
		temp=self.head
		strr=""
		while temp!=None:
			strr+=str(temp.key)+":"+str(temp.value)+" "
			temp=temp.next
		return strr[:-2]

	def size(self):
		temp=self.head 
		count=0 
		while temp!=None:
			count+=1
			temp=temp.next
		return count

#searchin
	def search(self,key):
		curr=self.head
		index=0
		while curr!=None:
			if curr.key==key:
				return index
			curr=curr.next
			index+=1
		return -1

#get node by index
	def get_node_at_index(self,index):
		curr=self.head
		pos=0
		if self.n<=index:
			return -1
		while curr !=None:
			if pos==index:
				return curr
			pos+=1
			curr=curr.next



class Dictionary:

	def __init__(self, capacity):
		#capacity is size of array that contain linkedlists and these array cells are
		#called bucketso this array is buckets
		#size contain that currently how many key value pairs we are having

		self.capacity=capacity
		self.size=0
		self.buckets=self.make_array(self.capacity)

		#if we do this like L=[Linkedlist()]*capacity but in the list all elements
		#will point to same linkedlist means all our same object


	def __setitem__(self,key,value):
		self.put(key,value)

	def __getitem__(self,key):
		self.get(key)

	def __delitem__(self,key):

		bucket_index=self.hash_function(key)
		self.buckets[bucket_index].delete_byvalue(key)

		self.size-=1
	
	def __str__(self):
		strr=''
		for i in self.buckets:
			strr+=i.traverse()+" "
		return strr

	def __len__(self):
		return self.size

	def make_array(self,capacity):
		L=[]

		for i in range(capacity):
			L.append(LinkedList())

		return L


	def put(self,key,value):
		bucket_index=self.hash_function(key)

		#now key value added to that index LL
		#case1 no node is there
		#case2 list is there but before adding we have to check whether key present in LL
		#case3 if not then add to tail

		node_index=self.get_node_index(bucket_index,key)

		if node_index==-1:
			#insert
			self.buckets[bucket_index].append(key,value)
			self.size+=1 #when new node added then do inc.

			load_factor= self.size/self.capacity
			print(load_factor)
			if load_factor >= 2: #we take load factor 2 generally
				self.rehashing()
		else:
			#update
			node=self.buckets[bucket_index].get_node_at_index(node_index)
			node.value=value

	def get(self,key):
		bucket_index=self.hash_function(key)
		res = self.buckets[bucket_index].search(key)

		if res==-1:
			return 'not present'
		else:
			node=self.buckets[bucket_index].get_node_at_index(res)
			return node.value 

	def get_node_index(self,bucket_index,key):
		node_index=self.buckets[bucket_index].search(key)

		return node_index



	def hash_function(self,key):
		hashed_key=abs(hash(key))%self.capacity
		return hashed_key

	def rehashing(self): #we create new array so hash function change and put every
		#element from old array and put that in new one so length of LL at every index
		#become less

		self.capacity=2*self.capacity #double the capacity
		old_buckets=self.buckets
		self.size=0
		self.buckets=self.make_array(self.capacity)


		for i in old_buckets:
			for j in range(i.size()):
				node=i.get_node_at_index(j)
				key_item=node.key
				value_item=node.value
				self.put(key_item,value_item)

		return




D1=Dictionary(4)
D1.put("python",34)
D1.put("java",56)
D1.put("c",500)
D1.put("ruby",200)
print(D1.buckets[0].traverse())
print(D1.buckets[1].traverse())
print(D1.buckets[2].traverse())
print(D1.buckets[3].traverse())

D1.put("c++",900)
D1.put("python",100)
D1.put("javascripts",210)
D1.put("R",110)
D1.put("php",910)
#now buckets become double so
print(D1.buckets[0].traverse())
print(D1.buckets[1].traverse())
print(D1.buckets[2].traverse())
print(D1.buckets[3].traverse())
print(D1.buckets[4].traverse())
print(D1.buckets[5].traverse())
print(D1.buckets[6].traverse())
print(D1.buckets[7].traverse())



print(D1['python']) #every time hash() function is giving different result for same key
#thats why getting function is not working correctly

del D1['c++'] #this is working correctly
print(D1)

print(len(D1))