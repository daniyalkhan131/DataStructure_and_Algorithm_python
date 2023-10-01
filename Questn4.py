#Given a linked list of characters. Write a python function to return a new string that is 
#created by appending all the characters given in the linked list as per the rules given 
#below.
# Rules ->
# Replace '* or '/ by a single space
# In case of two consecutive occurrences of* or / replace those two occurrences by a 
#single space and convert the next character to upper case
# Assume that ->
# There will not be more than two consecutive occurrences of * or '/'
# The linked list will always end with an alphabet
# Sample Input
# A,n,*,/,a,p,p,l,e,*,a,/,day,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,r,*,A,w,a,y
# Expected Output
# An Apple a day Keeps A Doctor Away


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


#don't directly do things by going with complex approach like here took two pointers
#instead try to solve with simple direct approach then if not possible then move to 
#complex thinking
	def string_convert(self):

		curr1=self.head.next
		curr2=self.head
		strr=''+str(curr2.data)
		flag=0
		while curr1!=None:
			if curr1.data=='/':
				strr+=' '
				flag=1
				if curr2.data=='*':
					flag=2
			elif curr1.data=='*':
				strr+=' '
				flag=1
				if curr2.data=='/':
					flag=2

			if flag==2:
				strr+=str(curr1.next.data).upper()
				flag=0
			elif flag==1:
				strr+=str(curr1.data)
			curr2=curr1
			curr1=curr1.next

		print(strr)

#this is correct implemented by me

#always check loop if else execution by printing at every condition
	def string_convert2(self):

		curr=self.head
		strr=''
		flag=0
		while curr!=None:
			if curr.data=='/':
				strr+=' '
				flag=1
				curr=curr.next
				print(1)
				if curr.data=='*'or curr.data=='/':
					flag=2
					curr=curr.next
					print(2)
		
			elif curr.data=='*':
				strr+=' '
				flag=1
				curr=curr.next
				print(3)
				if curr.data=='/'or curr.data=='*':
					flag=2
					curr=curr.next
					print(4)

			if flag==2:
				strr+=str(curr.data).upper()
				flag=0
				#curr=curr.next
				print(5)
			else:
				strr+=str(curr.data)
				#curr=curr.next
				print(6)

			curr=curr.next
		print(strr)


	#by campusx
	#he make changes in the LL while I created a string
	def string_convert3(self):

		temp=self.head
		while temp!=None:
			if temp.data=='*'or temp.data=='/':
				temp.data=' '

				if temp.next.data=='*'or temp.next.data=='/':
					temp.next.next.data=temp.next.next.data.upper()
					temp.next=temp.next.next
			temp=temp.next

	def traverse(self):
		temp=self.head
		strr=''
		while temp!=None:
			strr+=str(temp.data)
			temp=temp.next
		print(strr)





L=Linkedlist()
L.append('A')
L.append('n')
L.append('*')
L.append('/')
L.append('a')
L.append('p')
L.append('p')
L.append('l')
L.append('e')
L.append('*')
L.append('a')
L.append('/')
L.append('d')
L.append('a')
L.append('y')
L.append('*')
L.append('*')
L.append('k')
L.append('e')
L.append('e')
L.append('p')
L.append('s')
L.append('/')
L.append('*')
L.append('d')
L.append('o')
L.append('c')
L.append('t')
L.append('o')
L.append('r')
L.append('*')
L.append('A')
L.append('w')
L.append('a')
L.append('y')


L.traverse()
L.string_convert3()
L.traverse()




