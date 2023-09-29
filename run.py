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
    new_todo = [todo, due_date, "No"]
    tasks.append_row(new_todo)
    

def list_todos():
    if len(data) > 1:
        print("My ToDo List\n")
        for i, todo in enumerate(data[1:], start=1):
            print(
                f"{i}. ToDo: {todo[0]}, Due Date: {todo[1]}, Done: {todo[2]}")
    else:
        print("Your ToDo list is empty.")
    

def date_validation(date_str):
    try:
        if len(date_str) != 6:
            return False
        year, month, day = int(date_str[:2]), int(
            date_str[2:4]), int(date_str[4:])
        return 1 <= month <= 12 and 1 <= day <= 31
    except ValueError:
        return False
    

def mark_done():
    print("Mark Done")


def main():
    

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
            

        elif choice == "4":
            print("\n-------------------\nGood bye!\n-------------------\n")
            break

if __name__ == "__main__":
    main()
