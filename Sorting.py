def is_sorted(arr):
	for i in range(len(arr)-1):
		if arr[i]<=arr[i+1]:
			continue
		else:
			return 'not sorted'
	return 'sorted'

arr=[1,2,3,8,5,6]
print(is_sorted(arr))


def bubble_sort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-1-i):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
	return arr

#In adaptive sorting comes those algos that takes advantage of existing order in the
#input 
#bubble sort is addaptive sort like if already sorted or in some pass it become sorted
#then it will not go in the further pass thats why it is adaptive sorting
def bubble_sort_adaptive(arr):
	#flag=0 if we initilize here then for all passes it will be rmain flag=1 if
	#any elemets conditn satisfies for any passes

	for i in range(len(arr)-1):
		flag=0
		for j in range(len(arr)-1-i):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
				flag=1
		if flag==0:
			break
	return arr

#bubble sort is stable algorith

arr=[2,5,7,3,5,9,2,1]
print('bubble sort',bubble_sort(arr))
arr=[1,3,2,4,5]
print('bubble sort adaptive',bubble_sort_adaptive(arr))


def selection_sort(arr):
	for i in range(len(arr)):
		minn=i
		for j in range(i+1,len(arr)):
			if arr[minn]>arr[j]:
				minn=j
		arr[i],arr[minn]=arr[minn],arr[i]
	return arr
#selection sort is not adaptive sorting
#it is not stable algo
#benefit is we get sorting of i elements at ith pass

arr=[2,5,7,3,5,9,2,1]
print('selection sort',selection_sort(arr))

import random
arr1=[]
for i in range(1000):
	arr1.append(random.randint(1000,2000))
arr2=arr1[:]

import time
start=time.time()
bubble_sort_adaptive(arr1)
print('time taken by bubble sort is ',time.time()-start)

start=time.time()
selection_sort(arr2)
print('time taken by selection_sort is ',time.time()-start)
#selection sort is fast as less swappings




def merge_sort(arr,low,high):
	if low<high:
		mid=(low+high)//2
		merge_sort(arr,low,mid)
		merge_sort(arr,mid+1,high)
		merging(arr,low,mid,high)

def merging(arr,low,mid,high):
	l1=arr[low:mid+1]
	l2=arr[mid+1:high+1]

	#print(l1)   for seeing the working or diagnosing
	#print(l2)
	i,j,k=0,0,low
	while i<len(l1) and j<len(l2):
		if l1[i]<l2[j]:
			arr[k]=l1[i]
			i+=1
		else:
			arr[k]=l2[j]
			j+=1
		k+=1
	while i<len(l1):
		arr[k]=l1[i]
		i+=1
		k+=1
	while j<len(l2):
		arr[k]=l2[j]
		j+=1
		k+=1

#time complexity is O(nlogn)
#and space comp. is O(n) because new array and stack taking size O(logn)
#it is not adaptive
#python default sorting is tim sort it is based on merge sort and insertion sort


arr=[2,5,7,3,5,9,2,1]
merge_sort(arr,0,len(arr)-1)
print('merge sort',arr)



#monkey sort
# in this we randomly shuffle elements and see is list sorted or not, if not then do again

#time complexity is infinite not n! as we are not trying different combinations
import random
def monkey_sort(arr):
	#i=0
	while is_sorted(arr) != 'sorted':  # a lot of iterations it take as randomly done
		random.shuffle(arr)
		#print(i)
		#i+=1
	return arr



arr=[3,2,1,7,3,9]
print('monkey sort',monkey_sort(arr))


#sleep sort (the are fun questn that interviewr ask)
#every element is printed after that much seconds

import time
from threading import *
def sleep_sort(arr):
	return #I think we have to implement using multi-threading




#quick sort

def partition(arr,low,high):
	pivot=low
	i=low+1
	j=high

	while j>=i:
		# print('pivot',pivot)
		# print('pivot arr',arr[pivot])
		# print('i',i)
		# print('i arr',arr[i])
		# print('j',j)
		# print('j arr',arr[j])
		if arr[pivot]>=arr[i]:
			
			i+=1
		elif arr[pivot]<arr[j]:
			
			j-=1
		else:
			arr[i],arr[j]=arr[j],arr[i]
		#	print(arr)
		#print('------------------------')
	arr[j],arr[pivot]=arr[pivot],arr[j]
	pivot=j
	return pivot

def quick_sort(arr,low,high):

	if low<high:
		p=partition(arr,low,high)
		quick_sort(arr,low,p-1)
		quick_sort(arr,p+1,high)



arr=[2,5,7,3,15,9,11,1]
quick_sort(arr,0,len(arr)-1)
print('quick sort',arr)





