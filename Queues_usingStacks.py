#enqueue on S1 and dequeue on S2

class Stack:

	def __init__(self,size):
		self.size=size
		self.stack= [None]*size
		self.top=-1

	def push(self,value):
		if self.top==self.size-1:
			return 'Stack overflow'
		else:
			self.top+=1
			self.stack[self.top]=value

	def pop(self):
		if self.top==-1:
			return 'Stack empty'
		else:
			data=self.stack[self.top]
			self.top-=1
			return data

	def isempty(self):
		if self.top==-1:
			return True
		else:
			False

	def traverse(self):
		strr=''
		ptr=self.top
		while ptr!=-1:
			strr+='\n'+str(self.stack[ptr])
			ptr-=1
		return strr


class Queue:
	def __init__(self,n):
		self.S1=Stack(n)
		self.S2=Stack(n)
		self.l=[]

	def enqueue(self,value):
		self.S1.push(value)

	def dequeue(self):
		if self.S2.isempty():
			if self.S1.isempty():
				print('stack empty')
			else:
				while not self.S1.isempty():
					data=self.S1.pop()
					self.S2.push(data)
		temp=self.S2.pop()
		return temp

	def traverse(self):     #this i not properly implemented so change this
							#figure out the proper logic and then implement
		strr=''
		S3=Stack(10)
		S4=Stack(10)
		while not self.S2.isempty():
			data=self.S2.pop()
			S4.push(data)
			strr=strr+str(data)
		self.S2=S4
		while not self.S1.isempty():
			data=self.S1.pop()
			S3.push(data)
			strr=str(data)+strr
		self.S1=S3
		return strr


Q=Queue(10)
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
print(Q.traverse())
Q.dequeue()
Q.dequeue()
Q.dequeue()
print(Q.traverse())