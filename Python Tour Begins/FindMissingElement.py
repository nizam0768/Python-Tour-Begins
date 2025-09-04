def MissingElement(arr):
    length = len(arr)
    low, high = arr[0], arr[length-1]
    diff = low-0
    for i in range(length):
        if(arr[i] - i != diff):
            while(diff < arr[i] - i):
                print("Missing element is: ", i + diff)
                diff += 1
MissingElement([1, 2, 3, 4, 6, 9, 13, 15]) 
print("--------------Another example using Hasing Technique--------------")
# Another example
def MissingElementUsingHassing(arr):
    maxElement = max(arr)
    array = [0] * (maxElement+1)
    for num in arr:
        array[num] += 1
    for i in range(1, len(array)):
        if(array[i] == 0):
            print("Missing element is: ", i)

MissingElementUsingHassing([1, 2, 3, 4, 6, 9, 13, 15])

# Python Program to solve stock buy and sell by  
# exploring all possible pairs

def max_profit(prices):
    n = len(prices)
    res = 0

    # Explore all possible ways to buy and sell stock
    for i in range(n - 1):
        for j in range(i + 1, n):
            res = max(res, prices[j] - prices[i])
    
    return res

if __name__ == "__main__":
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(max_profit(prices))
