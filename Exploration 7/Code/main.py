class Student:
    classes = []
    age = 13

    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f'My name is {self.name}')

    def add_class(self, class_name):
        self.classes.append(class_name) 

    @classmethod
    def class_method(cls):
        print(f"{cls}'s class method has been called")
    
    @classmethod
    def change_classes(cls):
        cls.classes.append("Social Studies")
    
    @classmethod
    def change_age(cls):
        cls.age = 14

    @staticmethod
    def add(a, y):
        return a + y 

x = Student('X')
print(x.classes)
x.add_class("Social Studies")
print(x.classes)
x.talk()
print(x.age)
# x.talk(x)

om = Student('Om')
om.talk()
om.class_method()
# om.class_method(om)
# om.class_method(Student)

Student.class_method()
# Student.class_method(Student)

Student.change_classes()
Student.change_age()
Student.add(1, 3)

student = Student("student")
student.talk()
student.class_method()
print(student.classes)
print(student.age)
student.add(1, 3)
