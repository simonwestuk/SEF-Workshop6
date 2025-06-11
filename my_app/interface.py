from core import add_contact, view_all, update_contact, view_contact, view_full_details, remove_contact

def dash_line():
    print("-" * 60)

def main_menu():
    while True:
        print("\n" + "Contact Manager Main Menu".center(60, "-"))
        dash_line()
        print("1. Add New Contact")
        print("2. View All Contacts (Summary)")
        print("3. View All Contacts (Full Details)")
        print("4. View Specific Contact by ID")
        print("5. Update Contact")
        print("6. Remove Contact")
        print("X. Exit")
        dash_line()
        choice = input("Enter your option (1–6 or X to exit): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_all()
        elif choice == "3":
            view_full_details()
        elif choice == "4":
            view_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            remove_contact()
        elif choice.upper() == "X":
            confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
            if confirm == 'y':
                print("Thank you, goodbye.")
                break
            else:
                print("Returning to main menu.")
        else:
            print("Invalid option. Please enter a number from 1 to 6 or 'X' to exit.")
