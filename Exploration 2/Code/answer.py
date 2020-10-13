# 1) Take in 2 inputs
# 2) Add Those two inputs
# 3) Output the Sum

# 4) Take A user's name through input
# 5) Print out the reverse of it

# Sample input: {
#     Om --> Mo
#     1, 3 --> 4
# }

#1
num1 = int(input('First Number: '))
num2 = int(input('Second Number: '))
print(f'Sum of both numbers are {num1 + num2}')

#2
name = input('What is your name: ')
newName = name.lower() # You do not need this
print(f'Your name backwards is {newName[::-1]}')