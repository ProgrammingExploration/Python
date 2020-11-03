# Functions
def add(*values):
    sum = 0
    for i in values:
        sum += i
    
    print(sum)
    return sum

print(add(1, 2, 3, 4, 5))

def operation(*values, operator):
    if operator == 'add':
        sum = 0
        for i in values:
            sum += i # sum = sum + i
        return sum
    elif operator == 'multiply':
        product = 1
        for i in values:
            product *= i # product = product * i
        return product
    else:
        print("This is not a valid operator")

print(operation(1, 2, 3, 4, 5, 6, operator='add'))
print(operation(2, 3, 4, 5, operator='multiply'))

# Lambda
# def add(x, y):
#     return x + y

addLambda = lambda x, y: print(x + y)
addLambda(1, 3)

print((lambda x, y: x + y)(2, 3))

s = [1, 2, 3]

double = [(lambda x: x * 2)(x) for x in s]
# This works correctly
# for i in s:
#     double.append(i * 2)

# print(double)

# Classes
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print(f'My name is {self.name}')
        print(f'I am {self.age} years old')

    def study(self):
        print("Studying...")

    def __repr__(self):
        return self.name 

    # def __str__(self):
    #     return self.name

student = Student('Panda', 13)
student.study()

# Class and Staic Methods
class ClassMethod:
    def instance_method(self):
        print("Instance")

    @classmethod
    def class_method(cls):
        print(f'Called class_method of {cls}')
    
    @staticmethod
    def static_method():
        print(f'Called Static Method')

test = ClassMethod()
test.instance_method()
test.static_method()

ClassMethod.class_method()
print(ClassMethod)
ClassMethod.static_method()