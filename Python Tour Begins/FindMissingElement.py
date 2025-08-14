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

