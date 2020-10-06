# This is a comment

# Variables
x = 5 # Integer
y = 9.1 # Float

print(x)
print(y)
print('x')

# Type
print(type(y))

# Strings
name = 'Om Panda '

# F String
print(f'My name is {name}')

sentence = f'My name is {name}'
print(sentence)

# String Operations
print(name + name)
print(name * 10)

# Use a string like an array
print(name[0]) # The string characters start at 0
print(name[0:4]) # The last number is excluded
print(name[0:6:3]) # The last number is how much it skips
print(name[::-1])

# Input
user_name = input()
print(f'User name is {user_name}')

# Calculutor for checking lunar age
user_age = input()
product = int(user_age) * 12 # Int function takes in a variable and outputs a integer if possible
print(f'Your age in lunar years is {product}')