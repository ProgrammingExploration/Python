students = [
    {
        "name": "Om",
        "age": 13,
        "classes": ["Math", "Science", "English", "Social Studies"]
    },
    {
        "name": "Bob",
        "age": 50,
        "classes": ["Software Engineering"]
    },
    {
        "name": "Billy",
        "age": 8,
        "classes": ["Math", "English"]
    }
]

for s in students:
    name, age = s['name'], s['age']
    print(f'{name} is {age} years old')

def for_loop(list):
    for s in list:
        name, age = s['name'], s['age']
        print(f'{name} is {age} years old')

for_loop(students)