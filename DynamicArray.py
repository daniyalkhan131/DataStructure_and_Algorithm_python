#we will create dynamic array class in python using C data types
#and for that we will be using ctypes library

import ctypes

class MeraList:
	def __init__(self):
		self.size=1
		self.n=0

		#create a C type array with size=self.size
		self.A=self.__make_array(self.size)

	def __len__(self): #magic method
		return self.n

	def __str__(self): #this is for printing list with print functn       #magic method
		#[1,2,3,4]
		result=''
		for i in range(self.n):
			result=result+str(self.A[i])+','

		return '['+result[:-1]+']'

	def __getitem__(self,index): #magic method
		if 0<=index<self.n:
			return self.A[index]
		else:
			return 'IndexError - Index out of range'

	def __delitem__(self,pos): #magic method

		if 0<=pos<self.n:
			for i in range(pos,self.n-1):
				self.A[i]=self.A[i+1]

			self.n=self.n-1

	def append(self,item):
		if self.n==self.size :
			#resize
			self.__resize(self.size*2)

		#append
		self.A[self.n]=item
		self.n=self.n+1

	def pop(self):
		if self.n==0:
			return 'Empty List'

		print(self.A[self.n-1])
		self.n=self.n-1

	def clear(self):
		self.n=0
		self.size=1

	def find(self,item):
		for i in range(self.n):
			if self.A[i]==item:
				return i
		return 'ValueError - not in list'

	def insert(self,pos,item):
		if self.n==self.size:
			self.__resize(self.size*2)

		for i in range(self.n,pos,-1):
			self.A[i]=self.A[i-1]

		self.A[pos]=item
		self.n=self.n+1

	def remove(self,item):
		pos=self.find(item)

		if type(pos)==int:
			#delete
			self.__delitem__(pos)
		else:
			return pos


	def __resize(self,new_capacity):
		
		#create a new array with new capacity
		B=self.__make_array(new_capacity)
		self.size=new_capacity
		
		#copy the content of A to B
		for i in range(self.n):
			B[i]=self.A[i]

		#reassign
		self.A=B

	def __make_array(self,capacity):

		#creates a C type array(static,refrential) with size capacity
		return (capacity*ctypes.py_object)()



L=MeraList()
L.append("hello")
L.append(3.4)
L.append(True)
L.append(299)
L.append(99)


print(len(L ))

print(L)

print(L[0])
print(L[1])
print(L[2])
print(L[3])
print(L[4])

print()
L.pop()
print(L)

#L.clear()
#print(L)

print(L.find(True))

L.insert(1,'world')
print(L)

del L[3]
print(L)

L.remove('hello')
print(L)


#now do
#sort/min/max/sum
#extend
#negative indexing
#slicing
#merge