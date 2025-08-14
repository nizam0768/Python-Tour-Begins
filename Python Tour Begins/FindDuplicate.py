def FindDuplicate(arr):
    Array = [0] * (max(arr)+1)
    for num in arr:
        Array[num] += 1
    for i in range(1, len(Array)):
        if(Array[i]>1):
            print("Duplicate element is: ", i)

FindDuplicate([1, 2, 3, 4, 6, 9, 13, 15, 1, 2, 15])