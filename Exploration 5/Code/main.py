# Dictionaries
student = {
    "name": "Om",
    "age": 13,
    "classes": ["Math", "Science", "English"]
} 

students = [
    {
        "name": "Om",
        "age": "13"
    },
    {
        "name": "Bob",
        "age": 12
    }
]

for student in students:
    print(student["name"])

print(students[1]["name"])

var = {
    "x": 1,
    "y": 2
}

print(var["x"])

x, y, z, w = 1, 2, 3, 4
a = 5, 12
b, c = a

b, c = (5, 12)
print(c)

b, c = [5, 12]
print(b)

n = [4, 6, 3]
head, *tail = n
print(head)
print(tail)
*head, tail = n
print(head)
print(tail)

people = [
    ("Om", 42, "Mechanic"),
    ("Billy", 12, "Student"),
    ("Bob", 63, "Retired")
]

for name, age, _ in people:
    # Print Out The person's name and their age
    print(f'{name} is {age} years old')

def print_name():
    print("OM")

print_name()

def print_anything(s):
    print(s)

print_anything("My name is om")

def add(x, y):
    print(x + y)

add(1, 3)

def subtract(x, y):
    return x - y

difference = subtract(3, 1)