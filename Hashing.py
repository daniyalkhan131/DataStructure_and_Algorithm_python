#hashing gives fast searching
#in O(1)

#liner search tie complexity is O(N)
# binary search gives O(logN) but array should be sorted

#hashing function is used
#if our data is string then can create your own hashing function that just
#map that string data to an index value

#collision occur so to resolve this we do open addressing- linear probing and quadratic
#for open addressing no. of items<size of array
#close addressing- chaining

#if in chaining LL is greater then array then we have two tech. rehashing and LL->BST
#in rehshing if load factor is greater then we create a new array and then new hash functn
#and hashing is done on the data in old array to put in new one

#in LL->BST we convert LL to BST so searching is O(N)


#by using hashing we will make Dictionary class, this will behave like python dict

#linear probing using
class Dictionary:

	def __init__(self,size):
		self.size=size
		self.slots=[None]*self.size
		self.data=[None]*self.size

	def __setitem__(self,key,value): #magic method now we can use dict. notation
		self.put(key,value)

	def __getitem__(self,key):
		return self.get(key)

	def __repr__(self):
		strr=''
		for i,j in zip(self.slots,self.data):
			if i!=None:
				strr+=str(i)+':'+str(j)+','
		return '{'+strr[:-1]+'}'

#hash() in python give fixed value if given any string, tuple and if int then give int
	def hash_function(self,key):

		return abs(hash(key))%self.size


	def put(self,key,value):
		hash_value=self.hash_function(key)

		if self.slots[hash_value]==None:
			self.slots[hash_value]=key
			self.data[hash_value]=value 
		
		else:  
			#now two cases 1- same key is present
			#so change value not key
			if self.slots[hash_value]==key:
				self.data[hash_value]=value

			else:
				# 2- another key is present
				#linear probing is done means rehash and in next loc store

				new_hash_value=self.rehash(hash_value)

				while self.slots[new_hash_value]!=None and self.slots[new_hash_value]!=key:        
															#it is the possibility that
															#key present in the next further
															#locs
					new_hash_value=self.rehash(new_hash_value)

				if self.slots[new_hash_value]==None:
					self.slots[new_hash_value]=key
					self.data[new_hash_value]=value

				else:
					self.data[new_hash_value]=value 


	def get(self,key):

		#if we get key at index then return if not then search in increment fashion
		#we will stop if get None or starting position

		start_position=self.hash_function(key)
		current_position=start_position

		while self.slots[current_position] !=None:

			if self.slots[current_position]==key:
				return self.data[current_position]

			current_position=self.rehash(current_position)

			if current_position==start_position:
				return "Not Found"

		return "Not Found"


	def rehash(self,old_hash):
		return (old_hash+1)%self.size



		
D1=Dictionary(3)
print(D1.slots)
print(D1.data)
D1.put('python',42)
D1.put('java',46)

D1['C']=49
print(D1.slots)
print(D1.data)

D1['python']=100
print(D1.slots)
print(D1.data)


print(D1.get('python'))
print(D1.get('java'))
print(D1['C'])
print(D1['c'])


print()
print(D1)