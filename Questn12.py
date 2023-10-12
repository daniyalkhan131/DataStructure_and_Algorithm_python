#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and 
#choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. 
#If you cannot achieve any profit, return 0.

def stocks_max(price):
	maxx=0
	for i in range(len(price)):
		for j in range(i,len(price)):
			if price[j]-price[i] >maxx:
				maxx=price[j]-price[i]
				temp=(i+1,j+1)
	print(f'buy on day {temp[0]} and sell on day {temp[1]}')
	return maxx
# this is taking O(N^2) time we can do this in O(N)


def stocks_max(prices):
	maxx=0
	minn=prices[0]

	for i in range(1,len(prices)):
		maxx=max(maxx,prices[i]-minn)
		minn=min(minn,prices[i])
	return maxx





l=[7,17,1,2,3,4,5,6,345,6,34,88,343,33,9,5,4,5,7,6]
print(stocks_max(l))
