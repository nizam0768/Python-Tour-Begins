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