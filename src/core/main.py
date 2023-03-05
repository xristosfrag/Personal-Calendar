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
    # Get today's date and prompt the user for their activities
    today = datetime.date.today()
    activities = input(f"What did you do on {today}? ")

    # Insert a new row into the database
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO entries (date, activities) VALUES (?, ?)", (today, activities))
    conn.commit()
    conn.close()

def search_entries():
    # Prompt the user for a date and retrieve all rows from the database with that date
    search_date = input("Enter a date (YYYY-MM-DD): ")
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM entries WHERE date = ?", (search_date,))
    rows = c.fetchall()
    conn.close()

    # Display the rows to the user
    if len(rows) == 0:
        print("No entries found for that date.")
    else:
        for row in rows:
            print(f"{row[1]}: {row[2]}")


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