#celebrity problem
#from the matrix we have to find that member who dont know anyone but all knows him
#that means only one or zero person out of all is celebrity


#In a party of N people, only one person is known to everyone. Such a person may be present
#at the party, if yes, (s)he doesn’t know anyone at the party. We can only ask questions 
#like “does A know B? “. Find the stranger (celebrity) in the minimum number of questions.
#We can describe the problem input as an array of numbers/characters representing persons 
#in the party. We also have a hypothetical function HaveAcquaintance(A, B) which returns 
#true if A knows B, and false otherwise. How can we solve the problem? 

#MATRIX = { {0, 0, 1, 0}, {0, 0, 1, 0}, {0, 0, 0, 0}, {0, 0, 1, 0} }
#Output: id = 2
#Explanation: The person with ID 2 does not know anyone but everyone knows him

#Input:
#MATRIX = { {0, 0, 1, 0}, {0, 0, 1, 0}, {0, 1, 0, 0}, {0, 0, 1, 0} }
#Output: No celebrity
#Explanation: There is no celebrity.



#I made this and time complexity is O(n^3) and have some bugs so reolve it
def have_acquaintance(A,B,L):
	if L[A][B]==1:
		return True
	else:
		return False

def remove(i,j,L):
	L[i][j]=None
	jl[i]=None
	for k in range(len(L)):
		if L[k][i]==0:
			L[k][i]=None
	return L  

def celebrity(L):

	for i in range(len(L)):
		for j in range(len(L)):
			if have_acquaintance(i,j,L):
				L=remove(i,j,L)
	for i in L:
		print(i)
	for i in range(len(L)):
		if L[i][i]==0:
			return f'id = {i}' 
	return 'No celebrity'





L=[[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0] ]
jl=list(range(len(L)))
for i in L:
	print(i)
print(celebrity(L))
print(jl)


L=[[0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
for i in L:
	print(i)
print(celebrity(L))


L=[[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
for i in L:
	print(i)
print(celebrity(L))





print('-------------------------------')
#by campusx

#he use using approach selection by elimination using stacks
#it will solve problem in O(N)

#we check conditoin by taking top most two element from stack and based on the
#condition we push one of them, because only one of them is possible to push as
#problem is framed like that, in a problem we have to find out these things only


class Node:
	def __init__(self,value):
		self.data=value
		self.next=None

class Stack:
	def __init__(self):
		self.top=None
	
	def isempty(self):
		return self.top==None 

	def push(self,value):
		new_node=Node(value)
		new_node.next=self.top
		self.top=new_node

	def traverse(self):
		temp=self.top
		while temp!=None:
			print(temp.data)
			temp=temp.next

	def pop(self):
		if self.isempty():
			return 'stack empty'
		else:
			data=self.top.data
			self.top=self.top.next
			return data

	def size(self):
		curr=self.top
		count=0
		while curr!=None:
			count+=1
			curr=curr.next
		return count

def celebrity(M):

	S=Stack()
	for i in range(len(M)):
		S.push(i)

	while S.size()>1:
		a=S.pop()
		b=S.pop()

		if M[a][b]==1:
			#means a knows b so he can be celeb
			S.push(b)
		else:
			#means a dont know b so b can't be celeb as every one should know celeb
			S.push(a)
	
	k=S.pop()
	c1,c2=0,0
	for i in range(len(M)):
		c1+=M[k][i]
	for i in range(len(M)):
		c2+=M[i][k]
	if c1==0 and c2==len(M)-1:
		return f'id = {k}'
	else:
		return 'no celebrity'

	#or
	# for i in range(len(M)):
	# 	if i!=k:
	# 		if M[i][k]==0 or M[k][i]==1:
	# 			print('No one is celeb')
	# 			return
	# print("the celeb is",k)


L=[[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0] ]
#L=[[0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
#L=[[0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 0]]
for i in L:
	print(i)
print(celebrity(L))