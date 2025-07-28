import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
find_item = 3
for item in my_array:
    if item == find_item:
        print(f"Item {find_item} found in the array.")
