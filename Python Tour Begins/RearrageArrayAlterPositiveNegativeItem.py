# Python program to rearrange positive and negative numbers alternately
# using rotation in array

# Function to right rotate the subarray between out-of-place
# element and next opposite sign element
def rightRotate(arr, start, end):
    temp = arr[end]
    for i in range(end, start, -1):
        arr[i] = arr[i - 1]
    arr[start] = temp

# Function to rearrange the array
def rearrange(arr):
    n = len(arr)

    for i in range(n):
        
        # Check if the current positive element is out of place
        if arr[i] >= 0 and i % 2 == 1:
            
            # Find the next negative element and rotate the subarray
            # between these two elements
            for j in range(i + 1, n):
                if arr[j] < 0:
                    rightRotate(arr, i, j)
                    break
        
        # Check if the current negative element is out of place
        elif arr[i] < 0 and i % 2 == 0:
            
            # Find the next positive element and rotate the subarray
            # between these two elements
            for j in range(i + 1, n):
                if arr[j] >= 0:
                    rightRotate(arr, i, j)
                    break

if __name__ == "__main__":
    arr = [1, 2, 3, -4, -1, 4]

    rearrange(arr)
    print(" ".join(map(str, arr)))