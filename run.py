import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('my_todo_app')


tasks = SHEET.worksheet('tasks')
data = tasks.get_all_values()


def add_todo(todo, due_date):
    """
    Create a new ToDo row in the tasks worksheet that collects
    and adds input values from the todo and due_date variables.
    Set Done to "No" for every new ToDo.
    """

    new_todo = [todo, due_date, "No"]
    tasks.append_row(new_todo)
    

def list_todos():
    """
    Get all data from the tasks worksheet and check if the
    number of rows is more than 1 (header row). If True, 
    iterate through the worksheet list and assign all the row 
    data to the todo variable.

    To keep track of the row positions, enumerate is used to
    add a counter to each row. Starting from row 2 (index 1).
    https://www.w3schools.com/python/ref_func_enumerate.asp
    """

    if len(data) > 1:
        print("My ToDo List\n")
        for i, todo in enumerate(data[1:], start=1):
            print(f"{i}. ToDo: {todo[0]}, Due Date: {todo[1]}, Done: {todo[2]}")
    else:
        print("Your ToDo list is empty.")
    

def date_validation(date_str):
    """
    Validate input string for date. Check that length value
    is equal to 6 characters, if not (!=) return False. 
    Slice input data (yymmdd) between year, month, and day 
    and convert strings to integers. Validate sliced data to 
    be within valid date range and return if it's True.
    """

    try:
        if len(date_str) != 6:
            return False
        year, month, day = int(date_str[:2]), int(
            date_str[2:4]), int(date_str[4:])
        return 1 <= year <= 99 and 1 <= month <= 12 and 1 <= day <= 31
    except ValueError:
        return False
    

def mark_done(todo_index):
    """
    Function to update the DONE column in the worksheet from "No"
    to "Yes". To prevent users from updating a non-existing ToDo, 
    an if statement is checking that all ToDos is within the actual
    range (-1 for the heading). 
    
    If a ToDo is already marked in the third column (index 2), a
    new marking can't be done which is controlled by the if 
    statement that checks if the value is not equal (!=) to "Yes"
    """

    if 1 <= todo_index <= len(data) - 1:
        if data[todo_index][2] != "Yes":
            tasks.update_cell(todo_index + 1, 3, "Yes")
            print(f"Hurraaaay! '{data[todo_index][0]}' marked as done.")
        else:
            print("Ooops! You have already marked this one.")
    else:
        print(f"Invalid input. You have a total of {len(data[1:])} ToDos.\nPlease enter a \
        value between 1 and {len(data[1:])} to mark the corresponding list number.")


def main():
    """
    This function displays the main menu and handles the user input 
    thats validated by try/except blocks. 
    
    An if statement, below this function, uses the built-in variable 
    __name__ to control how this app is being executed; as a script in 
    the command line or imported to another app as a module: 
    https://docs.python.org/3/library/__main__.html
    """

    while True:
        print("\n-------------------\nMy Todo Menu:\n-------------------\n")
        print("1. Add ToDo")
        print("2. List ToDos")
        print("3. Mark ToDo as Done")
        print("4. Quit App")

        choice = input("\nEnter a choice (1-4) from the menu: ")

        if choice == "1":
            print("\n-------------------\n1. Add Todo:\n-------------------\n")
            todo = input("\nDescribe your ToDo:\n")
            due_date = input("\nGreat! Now, give it a due date (YYMMDD): ")
            if date_validation(due_date):
                add_todo(todo, due_date)
                print("\nPerfect! Your new ToDo was added successfully!")
            else:
                print(
                    "\nOh, something is wrong with the date format you entered.\nTry to write it as YYMMDD.")
        

        elif choice == "2":
            print("\n-------------------\n2. List ToDos:\n-------------------\n")
            list_todos()

        elif choice == "3":
            print("\n-------------------\n3. Mark ToDo as Done:\n-------------------\n")
            todo_index = input(
                "Enter the list number of the ToDo to mark as done: ")
            try:
                todo_index = int(todo_index)
                mark_done(todo_index)
            except ValueError:
                print(f"Invalid input. You have a total of {len(data[1:])} ToDos.\nPlease enter a \
                    value between 1 and {len(data[1:])} to mark the corresponding list number.")

        elif choice == "4":
            print("\n-------------------\nGood bye!\n-------------------\n")
            break

if __name__ == "__main__":
    main()
