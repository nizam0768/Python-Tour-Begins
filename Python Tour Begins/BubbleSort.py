def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize and stop early if no swaps happen
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Exit early if already sorted
    return arr

# Example usage
data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = bubble_sort(data)
print("Sorted array:", sorted_data)
