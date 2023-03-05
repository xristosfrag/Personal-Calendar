import datetime
import sqlite3

DB_FILE = "calendar.db"

def create_table():
    # Connect to the database and create the table if it doesn't exist
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS entries (id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE, activities TEXT)")
    conn.commit()
    conn.close()
    
def add_entry():
    # Get today's date
    today = datetime.date.today()

    # Prompt the user for their activities
    activities = input(f"What did you do on {today}? ")
    
    # Append the activities to the text file
    pathlib.Path("../../calendar/").mkdir(parents=True, exist_ok=True)
    with open("../../calendar/calendar.txt", "a+") as f:
        f.write(f"{today}: {activities}\n")

def view_entries():
    # Read the contents of the text file
    with open("calendar.txt", "r") as f:
        contents = f.read()

    # Display the contents to the user
    print(contents)


def main():
    while True:
        # Display the menu options
        print("1. Add a new entry")
        print("2. View previous entries")
        print("3. Quit")

        # Prompt the user for their choice
        choice = input("Enter your choice: ")

        # Call the appropriate function based on the user's choice
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()