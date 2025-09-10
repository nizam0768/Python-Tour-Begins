# List of integers
a = [1, 2, 3, 4, 5]

# List of strings
b = ['apple', 'banana', 'cherry']

# Mixed data types
c = [1, 'hello', 3.14, True]

print(a)
print(b)
print(c)

d = [12, 13, 43, 14, 17, 18, 20, 23, 43, 11]
d.append(100)
d.insert(2, 99)
z = d.pop(4)
del d[3]
print(z)
d.extend([200, 300, 400])
for i in d:
    print(i)

a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

# Count occurrences of 2
print(a.count(2))

# Count occurrences of 3
print(a.count(3))

a = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

# Create a list of unique items
b = list(set(a))

# Use list comprehension to count the frequency of each unique item
c = {item: a.count(item) for item in b}

# Print the frequency of each item
print(c)

a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

# Initial count is zero
count = 0

# Iterate over the list
for val in a:
  
  	# If num is equal to 3 
	if val == 3:
      
        # Increase the counter
		count += 1

print(count)

a = [1, 2, 3, (4, 5), 6, 7]

c = 0
for element in a:
    if isinstance(element, tuple):
        break
    c += 1

print(c)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)