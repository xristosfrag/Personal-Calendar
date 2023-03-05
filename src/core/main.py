import datetime

def add_entry():
    # Get today's date
    today = datetime.date.today()

    # Prompt the user for their activities
    activities = input(f"What did you do on {today}? ")

    # Append the activities to the text file
    with open("calendar.txt", "a") as f:
        f.write(f"{today}: {activities}\n")

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