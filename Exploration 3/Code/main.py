# If Statements
name = 'Om'
if name == 'Panda':
    print("Panda is my name")
elif name == 'Om':
    print("Om is my name")
else:
    print('Panda is not my name')

age = 13
if age > 13:
    print("Age is greater 13")
elif age == 13:
    print("Age is 13")
else:
    print("Age is less than 13")

if age != 12:
    print("Age is not 12")
else:
    print("Age is 12")

# Sets
l = ['a', 'b', 'c'] # List or Array
t = ('a', 'b', 'c') # Tuple
s = {'a', 'b', 'c'} # Sets

print(l)
print(t)
print(s)
print(l[1]) # The element's id start at 0

print(l[0:2]) 

# Change values is lists
l[0] = 'd'
l.append('e')
l.remove('b')
print(l)

# t[0] = 'd'
# print(t)
# Immutability (You cannot change the value)

s.remove('a')
s.add('d')
print(s)
# s[0] Sets do not store or remember the order that you assign them in 

# Applications
f1 = input("First Friend: ")
f2 = input("Second Friend: ")
f3 = input("Third Friend: ")

l_friends = [f1, f2, f3]

f4 = input("Friend that you lost: ")
l_friends.remove(f4)
print(l_friends)

friends = {"Om", "Bob", "Doug"}
abroad = {"Bob", "Doug"}

local_friends = friends.difference(abroad) # {"Om"}
print(local_friends)

local = {"Rolf"}
total_friends = local.union(abroad) # {"Rolf", "Bob", "Doug"}
print(total_friends)

art = {"Billy", "Doug", "Om", "Sam"}
math = {"Billy", "Doug", "Panda", "Joe"}

both = art.intersection(math)
print(both)