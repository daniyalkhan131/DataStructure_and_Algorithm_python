#though python list we can do all stack operations
#peak=L[-1]
#push=L.append()
#pop=L.pop()
#size=len(L)

#but we will implement using array concept as questn asked like language independent


class Stack:

	def __init__(self,size): #size because array are fixed in concept so need to tell
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

	def traverse(self):
		strr=''
		ptr=self.top
		while ptr!=-1:
			strr+='\n'+str(self.stack[ptr])
			ptr-=1
		return strr

	def traverse2(self): #made by campusx
		for i in range(self.top+1):
			print(self.stack[i],end=' ')


s=Stack(3)
print(s.stack)
s.push(1)
s.push(2)
s.push(3)
print(s.traverse())

print('popping',s.pop())
print(s.traverse())
s.traverse2()

