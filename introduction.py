#google use page rank algo
#DS is way of storing data efficiently, bascically organize them
#linear DS- arrays,linkedlist, stacks, queues, hashing
#nonlinear DS- trees, graphs

#Arrays
#arrays is used for multiple items stroing of same type in continuos memory loc.
#disadvantage is memory wastage as we have to define mem size before usage(fixed size)
#it is homogenous (same type of things stored)
#we can make heterogenous arrays by using refrential arrays
#call by value used for simple array that is homogenous
#we store our data anywhere in the memory and then store their addresses in the array 
#sequence wise and this is call by reference
#now we can store different type of info as our arrray contain address that is same type
#python list is refrential array
#it is slow and need extra memory
#now we have to solve fixed size problem of arrays
#for that we use dynamic array
#in dynamic array what is done is that like we have static array of size 1 so when we add
#2nd item then a new static array created of double size and previous array content got
#copied and again when it got full then new static of double size created and then
#content got copied and same thing....
#dynamic array is concept that we made from static array


#python list is dynamic array

import sys

L=[]
print(f"size is {sys.getsizeof(L)}")
L.append("hello")
print(f"list is {L}")
print(f"size is {sys.getsizeof(L)}")

L.append("world")
print(f"list is {L}")
print(f"size is {sys.getsizeof(L)}")

L.append(1)
print(f"list is {L}")
print(f"size is {sys.getsizeof(L)}")

L.append(2)
print(f"list is {L}")
print(f"size is {sys.getsizeof(L)}")

L.append(3)
print(f"list is {L}")
print(f"size is {sys.getsizeof(L)}")

#can see how the list is getting bigger

print()
L1=[]
for i in range(100):
	print(i,sys.getsizeof(L1))
	L1.append(i)