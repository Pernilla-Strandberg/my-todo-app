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


def add_todo():
    

def list_todos():
    

def date_validation():
    

def mark_done():
    


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
        

        elif choice == "2":
            print("\n-------------------\n2. List ToDos:\n-------------------\n")
            

        elif choice == "3":
            print("\n-------------------\n3. Mark ToDo as Done:\n-------------------\n")
            

        elif choice == "4":
            print("\n-------------------\nGood bye!\n-------------------\n")
            break

if __name__ == "__main__":
    main()
