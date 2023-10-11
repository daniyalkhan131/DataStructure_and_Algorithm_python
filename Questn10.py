#Given an integer array nums, return an array answer such that answer[i] is 
#equal to the product of all the elements of nums except nums [i]

def product_except(arr):
	answer=[None]*len(arr)
	result=1
	for i in arr:
		result*=i
	for i in range(len(answer)):
		answer[i]=result//arr[i]
	return answer

nums=[1,2,3,4,5,6,7]
print(product_except(nums))
