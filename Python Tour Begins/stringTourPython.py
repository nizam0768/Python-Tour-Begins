import datetime
# String Slicing

str = "GeeksforGeeks"
print(str[0:4])  # Output: Geeks
print(str[5:])    # Output: forGeeks

#str[0] = 'I'
#print(str)  # This will raise an error because strings are immutable in Python

str = "I am a geek" + " and I love coding"
print(str)  # Output: I am a geek and I love coding
print(len(str))  # Output: 30
print(str.upper())
print(str.lower())

#strip 
strStrip = "   Hello, World!   "
print(strStrip.strip())  # Output: Hello, World!

strReplace = "Hi, I am Tom"
print(strReplace.replace("Tom", "Nizam"))

# COncatanation and Repetitive Strings
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)  # Output: Hello World
print(str1 * 3)  # Output: HelloHelloHello

# Formatting Strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# String Methods
str = "Python Programming"
print("Python" in str)
print("GfG" in str)

s = "Hello, Python!"

print(s[0:5])  # Output: Hello
print(s[7:])    # Output: Python!
print(s[:-5])  # Output: Hell

s = "abcdefghijklmnopqrstuvwxyz"
print(s[::2])  # Output: acegikmoqsuwy
print(s[-4:]) 
print(s[:-3])
print(s[-5:-2])  # Output: vwx
print(s[-8:-1:3])
print(s[::-1])

# Print Variables using f-strings

today = datetime.datetime.today()
print(f"{today: %B %d, %Y}")

english = 78
maths = 56
hindi = 85

print(f"Ram got total marks {english + maths + hindi} out of 300")
print(f"newline: {ord('\n')}")
print(f"{{{{Hello, Mohammad}}}}")
print(f"{{Hello, Geek}}")

# Printing Dictionaries
student = {
    "name": "John",
    "age": 20,
    "course": "Computer Science"
}
print(f"name of student {student['name']} is {student['age']} years olg. He is studying {student['course']}.")