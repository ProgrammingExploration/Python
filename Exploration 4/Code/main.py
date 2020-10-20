# Booleans and Operative Booleans
x = 5

boolean = x == 5
if boolean: 
    print("x is 5")

# if x == 5:
    # print("x is 5)

# ==, >=, >, <=
name = 'Om'
if name == 'Om':
    print("Hello")

newName = 'Om'

# Python Storage

'''
    'om' --> newerName
    'Om' --> Name --> newName
'''

if name is newName:
    print("name is name")

# In
ages = [12, 13, 14, 15]
age = 18
if age in ages:
    print("age is qualified")

s = { 'Om', 'Panda', 'Billy', 'Bob' }
r = input("What do you want to remove\n")
if r in s:
    s.remove(r)
    print(s)
else:
    print("Sorry your input is not in the set")

# While
'''
    if (Boolean):
        kajsdlf
    else:
        klasdfk
    
    while (Boolean):
        jakjsdkfjk
'''


# Guessing
import random
y = random.randint(0, 100)
print(y)

guesses = 0

while True:
    user_input = input("Would you like to play the game (Y/n)")
    guesses += 1
    if user_input in ['N', 'n']:
        break
    number = int(input("What is your guess\n"))
    if number == y:
        print("YOU WON!!")
        print(f"It took you {guesses} amount of tries")
        break
    elif number - y in [1, -1]:
        print("You were one off, so close")
    else:
        print("Sorry it is wrong"