# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table."
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# MHamilton,11.14.21,Added code to complete assignment 5
# MHamilton,11.16.21,Added new code for relative paths; fixed writing bug
# ------------------------------------------------------------------------ #

# -- Paths -- #
import os                                   # Used to define relative paths below

# -- Data -- #
# declare variables and constants
dirname = os.path.dirname(__file__)         # The current directory where the script is located
objFile = os.path.join(dirname, "ToDoList.txt")    # A relative file reference to the current To Do list
strData = ""                                # A row of text data from the file
dicRow = {}                                 # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []                               # A list that acts as a 'table' of rows
strMenu = ""                                # A menu of user options
strChoice = ""                              # A Capture the user option selection
itemName = ""                               # A new to-do item input by user
itemPriority = ""                           # A priority attached to the new item
itemRemoved = ""                            # A Boolean noting whether an item was removed


# -- Processing -- #
# Step 1 - Here we load any data we have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
try:
    todolist = open(objFile, "r")
    for row in todolist:
        lstRow = row.split(",") # Note-- this returns a list!
        dicRow = {"Task":lstRow[0], "Priority":lstRow[1].strip()}
        lstTable.append(dicRow)
    todolist.close()
except:
    print("No existing file found!")   # Print error message if no file exists.
pass

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == "1"):
        if len(lstTable) == 0:
            print("No items listed.")
        else:
            for rowDic in lstTable:
                print("Task:", rowDic["Task"], ", Priority: ", rowDic["Priority"])
            continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == "2"):
        print("Please enter a to-do item and its priority: ")
        itemName = input("Enter a to-do item: ")
        itemPriority = input("Enter a priority: ")
        # insert into data table
        lstTable.append({"Task":itemName, "Priority":itemPriority})
        continue

   # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == "3"):
        print("Please enter the item you would like to remove: ")
        name = input("Enter name here: ")
    # First set removed parameter as false, then loop through table and identify item to be removed
        itemRemoved = False
        for dicRow in lstTable:
            if dicRow["Task"] == name.strip():
                lstTable.remove(dicRow)
                print("Item removed!")
                # Here we must set itemRemoved to True to not print the following block
                itemRemoved = True
        if itemRemoved == False:
            print("Item not found.")
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == "4"):
        # Process the data into a file
        todolist = open(objFile, "w")
        for rowDic in lstTable:
            todolist.write(rowDic["Task"] + "," + rowDic["Priority"] + "\n")
        todolist.close()
        # Display a message to the user
        print("Data saved to file!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Goodbye!")
        break  # and Exit the program
