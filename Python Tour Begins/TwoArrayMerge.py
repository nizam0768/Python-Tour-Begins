def MergeArrays(arr1, arr2):
    """
    Merges two sorted arrays into one sorted array.
    
    Parameters:
    arr1 (list): First sorted array.
    arr2 (list): Second sorted array.
    
    Returns:
    list: Merged sorted array.
    """
    merged_array = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
            
    # Append remaining elements
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])
    
    return merged_array
print(MergeArrays([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
