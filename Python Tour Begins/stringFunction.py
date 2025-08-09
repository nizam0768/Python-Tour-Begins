#string function in python
sentence1 = "My Name is Khan. Embarking on a new journey."
sentence2 = ['I', 'am', 'a', 'software', 'engineer.']
capatilized_sentence1 = sentence1.capitalize()
print(' '.join(sentence2))  # Output: I am a software engineer. My Name is Khan. Embarking on a new journey.
print(capatilized_sentence1)  # Output: My name is khan.
print(sentence1.upper())  # Output: MY NAME IS KHAN.
print(sentence1.lower())  # Output: my name is khan. embarking on a new journey.
print(sentence1.title())  # Output: My Name Is Khan. Embarking On A New Journey.
print(sentence1.swapcase())  # Output: mY nAME IS kHAN. eMBARKING ON A NEW JOURNEY.
print(sentence1.replace("Khan", "Khan Academy"))  # Output: My Name is Khan Academy. Embarking on a new journey.
print(sentence1.split())  # Output: ['My', 'Name', 'is', 'Khan.', 'Embarking', 'on', 'a', 'new', 'journey.']
print(sentence1.split(" "))  # Output: ['My', 'Name', 'is', 'Khan.', 'Embarking', 'on', 'a', 'new', 'journey.']
print(sentence1.split("a"))  # Output: ['My N', 'me is Khan. Emb', 'rking on ', ' new journey.']
#print(sentence2.count("e"))  # Output: 5
#print(sentence2.find("software"))  # Output: 10


# Python string format methods
a = "My nam is khan"
b = 25
msg = "{} and I am {} years old.".format(a,b)
print(msg)
def formatted_table(a, b):
    for i in range(a, b):
        print("{:6d} {:6d} {:6d} {:6d}".format(i, i**2, i**3, i**4))

formatted_table(3, 10)