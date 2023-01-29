#import libraries
from tkinter import *
from datetime import date

#initialize tkinter window
root = Tk()
root.geometry('280x280')
root.resizable(0,0)
root.title('Age Calculator')

#create a label for displaying the result
statement = Label(root)

#defining a function for calculating age
def agecalculator():
    global statement

    #clear the previous result
    statement.destroy() 

    #get the current date
    today = date.today() 

    #get the birth date from the user input
    birth_date = date(int(year_value.get()), int(month_value.get()), int(date_value.get()))

    #calculate the age
    age = today.year - birth_date.year 
    if  today.month < birth_date.month or today.month == birth_date.month and today.date < birth_date.day:
        age -= 1
    
    #display the result
    statement = Label(text = f"{name_value.get()}'s age is {age}.")
    statement.grid(row = 6, column = 1, pady = 10)

#create a label for name
l1 = Label(text = "Name:")
l1.grid(row = 1, column = 0)
#create an entry for name
name_value = StringVar()
name_entry = Entry(root, textvariable = name_value)
name_entry.grid(row = 1, column = 1, pady = 10)

#create a label for year
l2 = Label(text = "Year: ")
l2.grid(row = 2, column = 0)
#create an entry for year
year_value = StringVar()
year_entry = Entry(root, textvariable = year_value)
year_entry.grid(row = 2, column = 1, pady = 10)

#create a label for month
l3 = Label(text = "Month: ")
l3.grid(row = 3, column = 0)
#create an entry for month
month_value = StringVar()
month_entry = Entry(root, textvariable = month_value)
month_entry.grid(row = 3, column = 1, pady = 10)

#create a label for date
l4 = Label(text = "Date: ")
l4.grid(row = 4, column = 0)
#create an entry for date
date_value = StringVar()
date_entry = Entry(root, textvariable = date_value)
date_entry.grid(row = 4, column = 1, pady = 10)

#create a button for calculating age
button = Button(text = "Calculate Age", command = agecalculator)
button.grid(row = 5, column = 1)

#start the main event loop
root.mainloop()