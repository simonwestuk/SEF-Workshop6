from data import contacts, next_id
import validator

def view_all():
    print("ID".ljust(6), "Name".ljust(15), "Number".ljust(15), "Email".ljust(25), "Company".ljust(20))
    print("-" * 85)

    for contact in contacts:
        print(
            str(contact['id']).ljust(6),
            contact['name'].ljust(15),
            contact['number'].ljust(15),
            contact['email'].ljust(25),
            contact['company'].ljust(20)
        )

def view_full_details():
    print("\nFull Contact Details:")
    for contact in contacts:
        print(f"\nID: {contact['id']}")
        print(f"Name: {contact['name']}")
        print(f"Number: {contact['number']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
        print(f"Date of Birth: {contact['date_of_birth']}")
        print(f"Company: {contact['company']}")
        print(f"Notes: {contact['notes']}")
        print("-" * 40)

def add_contact():
    global next_id
    contact = {
        "id": next_id,
        "name": validator.validate_name(),
        "number": validator.validate_number(),
        "email": validator.validate_email(),
        "address": validator.validate_address(),
        "date_of_birth": validator.validate_date_of_birth(),
        "company": validator.validate_company(),
        "notes": validator.validate_notes()
    }
    contacts.append(contact)
    next_id += 1
    print("Contact added successfully.\n")

def update_contact():
    id = validator.validate_id()
    found = False
    for contact in contacts:
        if contact["id"] == id:
            print("Enter new details (leave blank to keep current value):")
            new_name = input(f"Name [{contact['name']}]: ") or contact['name']
            new_number = input(f"Number [{contact['number']}]: ") or contact['number']
            new_email = input(f"Email [{contact['email']}]: ") or contact['email']
            new_address = input(f"Address [{contact['address']}]: ") or contact['address']
            new_dob = input(f"Date of Birth [{contact['date_of_birth']}]: ") or contact['date_of_birth']
            new_company = input(f"Company [{contact['company']}]: ") or contact['company']
            new_notes = input(f"Notes [{contact['notes']}]: ") or contact['notes']

            # Re-validation
            contact['name'] = validator.validate_name() if new_name != contact['name'] else contact['name']
            contact['number'] = validator.validate_number() if new_number != contact['number'] else contact['number']
            contact['email'] = validator.validate_email() if new_email != contact['email'] else contact['email']
            contact['address'] = new_address
            contact['date_of_birth'] = new_dob
            contact['company'] = new_company
            contact['notes'] = new_notes

            print(f"{id} updated successfully.")
            found = True
            break
    if not found:
        print("ID not found.")
      
def view_contact():
  id = validator.validate_id()
  found = False
  for contact in contacts:
      if contact["id"] == id:
          print("\nContact Details:")
          print(f"ID: {contact['id']}")
          print(f"Name: {contact['name']}")
          print(f"Number: {contact['number']}")
          print(f"Email: {contact['email']}")
          print(f"Address: {contact['address']}")
          print(f"Date of Birth: {contact['date_of_birth']}")
          print(f"Company: {contact['company']}")
          print(f"Notes: {contact['notes']}")
          print("-" * 40)
          found = True
          break
  if not found:
      print("Contact not found.")

def remove_contact():
  id = validator.validate_id()
  for i, contact in enumerate(contacts):
      if contact["id"] == id:
          confirm = input(f"Are you sure you want to delete contact '{contact['name']}'? (y/n): ").lower()
          if confirm == 'y':
              del contacts[i]
              print("Contact removed successfully.")
          else:
              print("Deletion cancelled.")
          return
  print("Contact not found.")