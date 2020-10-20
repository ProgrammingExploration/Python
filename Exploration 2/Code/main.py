# This is a comment

# Variables
x = 5 # Integer
y = 9.1 # Float

print(x)
print(y)
print('x') # Result to Printing the literal string X

# Type
print(type(x))
type(x) # Return Integer <class 'int'>

# Strings
name = 'Om Panda '

# F String
print(f'My name is {name}')

sentence = f'My name is {name}'
print(sentence)

# String Operations
print(name + name) # Om Panda Om Panda
print(name * 10) 

# Use a string like an array
# name = 'Om Panda '
print(name[0]) # The string characters start at 0
print(name[0:4]) # The last number is excluded
print(name[0:6:2]) # The last number is how much it skips
print(name[::-1]) # Reverse Order

# Input
user_name = input()
print(f'User name is {user_name}')

# Calculutor for checking lunar age
user_age = input() # Returns String
product = int(user_age) * 12 # Int function takes in a variable and outputs a integer if possible
print(f'Your age in lunar years is {product}')

age = int(input('How old are you? \n'))
print(f'Lunar age is {age}')