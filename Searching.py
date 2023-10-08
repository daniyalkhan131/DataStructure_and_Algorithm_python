def linear_search(arr, item):
	for i in range(len(arr)):
		if arr[i]==item:
			return i 
	return -1


def binary_search(arr,item):

	i=0
	j=len(arr)-1
	mid=(i+j)//2

	while j>=i :
		if arr[mid]==item:

			return mid 
		elif arr[mid]>item:
			j=mid-1

		else:
			i=mid+1

		mid=(i+j)//2

	return -1

def binary_search_recursion(arr,low,high,item):

	if low<=high:
		mid=(low+high)//2

		if arr[mid]==item:
			return mid
		elif arr[mid]>item:
			return binary_search_recursion(arr,low,mid-1,item) #if we dont put return 
			#then it will return on -1 and ans given will be -1
		else:
			return binary_search_recursion(arr,mid+1,high,item)
	return -1

arr1=[5,2,8,4,9,1,3]
arr2=[1,2,3,4,5,6,7,8,9]
print(linear_search(arr1,9))
print(binary_search(arr2,7))
print(binary_search_recursion(arr2,0,len(arr2)-1,7))

#for binary search needed O(nlogn+logn) and for linear search need O(n)
#so amortized comes into play like if we want to do k times and k is large very so
# nlogn become negligible so we get O(logn) as only once we need to do sorting and large
#number of searching we can do with O(logn) rather than O(n)

