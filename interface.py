from core import add_contact, view_all, update_contact

def dash_line():
   print(55*"-")

def main_menu():
  while True:
    print("Main Menu".center(55,"-"))
    dash_line()
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Update Contact")
    print("X. Exit")
    dash_line()
    choice = input("Enter option:")

    if choice == "1":
      add_contact()
    elif choice =="2":
      view_all()
    elif choice =="3":
      update_contact()
    elif choice.upper() == "X":
      print("Thank you, goodbye.")
      break
