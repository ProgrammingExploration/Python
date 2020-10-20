import random

def randomize(i):
    return str(i)

n = randomize(random.randint(0, 100))

while True:
    user_input = input('Do you want to play (Y/n)')
    if user_input in ['N', 'n']:
        break
    nu = input("What is your guess: ")
    if nu == n:
        print("You won")
        break
    elif nu in n:
        print("Very Close")
    else:
        print("You lost")