# Inheritance 
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        return f'Device {self.name} is connected by {self.connected_by}'
    
    def disconnect(self):
        self.connected = False
        print("Disconnected")

# d = Device("Phone", "USB")
# print(d.name)
# d.disconnect()
# print(d.connected)

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_page = capacity
    
    def __str__(self):
        return f"{super().__str__()} ({self.remaining_page} pages remaining)"
    
    def print_paper(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print(f'Printing {pages} pages.')
        self.remaining_page -= pages

p = Printer("Printer", "USB", 200)
p.disconnect()
print(p.name)
print(p)
p.print_paper(20)
print(p.remaining_page)

# Composition
class Book:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'Book {self.name}'

book1 = Book("Harry Potter 1")
book2 = Book("Harry Potter 2")

class BookShelf:
    def __init__(self, *books):
        self.books = books
    
    def __str__(self):
        return f'BookShelf with {len(self.books)} books'

    def for_loop(self):
        for book in self.books:
            print(book.name)

bookshelf = BookShelf(book1, book2)
bookshelf.for_loop()
