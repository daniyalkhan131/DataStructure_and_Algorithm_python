#Given an integer array nums, move all 0's to the end of it while maintaining 
#the relative order of the non-zero elements.Note that you must do this in-place 
#without making a copy of the array.

def place_zeros(arr):
	zeros=0
	i=0
	j=0

	while j<len(arr):
		while i==j and j<len(arr) and arr[j]!=0:
			i+=1
			j+=1
		while arr[j]==0:
			zeros+=1
			j+=1
		if zeros!=0 and arr[j]!=0:
			arr[i]=arr[j]
			i+=1

		if i!=j:
			j+=1
	while zeros!=0:
		arr[i]=0
		zeros-=1
		i+=1
	return arr


#this is the perfect code I wrote by thinking myself
#with O(N) time comp.

def place_zeros(arr):
	zeros=0
	i=0

	while i<len(arr):

		if arr[i]==0:
			zeros+=1
		else:
			arr[i-zeros]=arr[i]
		i+=1
	

	j=len(arr)-1
	while zeros>0:
		arr[j]=0
		zeros-=1
		j-=1

	return arr

#what I found online
def pushZerosToEnd(self,arr, n):
   	zeros=0
   	i=0
    
   	while i<len(arr):
    
   		if arr[i]!=0:
   			arr[zeros]=arr[i]
   			zeros+=1
   		i+=1
    	
    
   	while zeros<len(arr):
   		arr[zeros]=0
   		zeros+=1
    
   	return arr


nums=[1,2,0,0,0,3,4,5]

print(place_zeros(nums))