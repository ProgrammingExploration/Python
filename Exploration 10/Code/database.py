import sqlite3
from tkinter import *

root = Tk()
root.title('Database')

conn = sqlite3.connect('address_book.db')

c = conn.cursor()

# Create a table
c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )
""")

# Submit Function
def submit():
    # Creating a database or connect to one
    connection = sqlite3.connect('address_book.db')

    # Create Cursor
    c = connection.cursor()
    #Insert Into Table
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'city': city.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        }
    )

    # Commit Changes
    connection.commit()

    # Close Connection
    connection.close()

    # Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Query Function
def query():
    # Creating a database or connect to one
    connection = sqlite3.connect('address_book.db')

    # Create Cursor
    c = connection.cursor()
    
    # Query Database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)
    
    print_records = ''

    for record in records[0]:
        print_records += str(record) + "\n"
    
    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    # Commit Changes
    connection.commit()

    # Close Connection
    connection.close()



# Create Text Box 
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# Create Label
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(row=5, column=0)

# Submit Button
submit_btn = Button(root, text="Add Record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create a query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

root.mainloop()
