# Rotate array
def rotate_array(arr, k):
    n = len(arr)
    for i in range(k):
        first = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = first
 
arr = [1, 2, 3, 4, 5]
d = 2
rotate_array(arr, d)

for i in range(len(arr)):
    print(arr[i], end=" ")

print()
# Wave array
def wave_array(arr):
    n = len(arr)
    for i in range(0, n-1, 2):
        if i < n-1 and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

arr = [1, 2, 3, 4, 5]
print(wave_array(arr), end=" ")