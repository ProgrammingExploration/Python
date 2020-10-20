# Part 1
f1 = input()
f2 = input()
f3 = input()
f4 = input()
f5 = input()

s = { f1, f2, f3, f4, f5 }
print(s)

r = input()
s.remove(r)

a = input() 
s.add(a)

print(s)

# Challenge
i1 = int(input()) 
i2 = int(input()) 
i3 = int(input()) 
i4 = int(input()) 
i5 = int(input()) 

d = [i1, i2, i3, i4, i5]

for f in d:
    print(f + 1) 

# Part 2 
s1 = { 'Om', 'Panda', 'Shivam' }
print(s1.difference(s))
print(s1.union(s))
print(s1.intersection(s))