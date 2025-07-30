def BinarySearch(arr, target):
    left=0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1    

arr = [1, 2, 3, 4, 5,17, 19, 23, 27, 45, 67, 89]
find_item = 67
index = BinarySearch(arr, find_item)
if index != -1:
    print(f"Item {find_item} found at index {index}.")
else:
    print(f"Item {find_item} not found in the array.")