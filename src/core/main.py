import datetime
import sqlite3

DB_FILE = "../../database/calendar.db"

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

def search_entries(date):
    # Prompt the user for a date and retrieve all rows from the database with that date
    search_date = ""
    if date == "":
        search_date = input("Enter a date (YYYY-MM-DD): ")
    else:
        search_date = date

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Display the rows to the user
    c.execute("SELECT id, activities FROM entries WHERE date = ?", (search_date,))
    rows = c.fetchall()
    conn.close()

    # Display the rows to the user and return the ID of the selected row, or None if no rows were found
    if len(rows) == 0:
        print("No entries found for that date.")
        return None
    else:
        if date == "":
            for row in rows:
                print(f"{row[0]}: {row[1]}")
        return rows


def update_entry():
    # Prompt the user for a date and retrieve the corresponding activities from the database
    search_date = input("Enter a date (YYYY-MM-DD): ")
    activities = search_entries(search_date)
    if activities is []:
        return

    # Ask the user if they want to update all or part of the activities
    print(f"Activities for {search_date}:")
    for row in activities:
        print(f"Id: {row[0]}, Entry: {row[1]}")
    choice = input("Select id of entry to update or type 'x' to exit: ")

    # Update the corresponding row in the database based on the user's choice
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT activities FROM entries WHERE id = ?", (choice,))
    row = c.fetchone()
    activities = row[0]


    
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    if choice == "1":
        new_activity = input("Update your activity: ")
        c.execute("UPDATE entries SET activities = ? WHERE id = ? and date = ?", (new_activity, choice, search_date))
    elif choice == 'x':
        pass
    else:
        print("Invalid choice.")
    conn.commit()
    conn.close()


def main():
    create_table()
    while True:
        # Display the menu options
        print("1. Add a new entry")
        print("2. Search entries")
        print("3. Update an entry")
        print("4. Quit")

        # Prompt the user for their choice
        choice = input("Enter your choice: ")
        print()

        # Call the appropriate function based on the user's choice
        if choice == "1":
            add_entry()
        elif choice == "2":
            search_entries("")
        elif choice == "3":
            update_entry()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()