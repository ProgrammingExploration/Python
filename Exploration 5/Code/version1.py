# Version 1
p = "This blog post is directed to junior and senior developers that are trying to learn a programming language or even a concept on their own and is struggling or using the technique I am about to explain. I have come across several beginner programmers and I love when I see them stumble across a great youtube channel that explains really well or stack overflow solutions, but although it might seem like it is helping significantly now, it will drag you down and slow you down as a developer. See, the stack overflow solutions and youtube tutorials, may be helpful, but all the videos are helping you in increasing the speed of your typing to follow along with the video. This method is what I call the drugs of software engineering. Once you start, you can’t stop, and it may be great now, but it will be horrible in the long-run. See, beginners for not only programming, but for just one language, will get stuck with an error or a logical bug, and instead of reading the code again to debug, the first instinct is to look it up, and as the cycle repeats, you may be building up your portfolio with amazing projects, but it isn’t building your knowledge. So, you may be agreeing with me right now or you may be disagreeing with me, but either way, I would look extremely stupid if I were to not give you my method of avoiding this problem, buy still gaining knowledge and understanding, and also building up a portfolio."
print(p)
print("Randomizing...")
def randomize(p):
    array = p.split(' ')
    '''
        p = 'Om is awesome'
        array = p.split(' ')
        print(array)
        ['Om', 'is', 'awesome']
    '''
    array[0]
    import random
    i = random.randint(0, len(array) - 1)
    return array[i] 

string = randomize(p)
while True:
    user_input = input("Do you want to play (Y/n)\n")
    if user_input in ('N', 'n'):
        break
    i = input("Your Guess: ")
    if i == string:
        print("You won")
        break
    elif i in string:
        print("You were so close")
    else:
        print("You lost")