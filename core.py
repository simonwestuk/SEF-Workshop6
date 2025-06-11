from data import contacts, next_id
import validator

def view_all():
    print("ID".ljust(6), end='')
    print("Name".ljust(15), end='')
    print("Number".ljust(15), end='')
    print("Email")
    print("-" * 55)

    for contact in contacts:
        print(str(contact['id']).ljust(6), end='')
        print(contact['name'].ljust(15), end='')
        print(contact['number'].ljust(15), end='')
        print(contact['email'])

def add_contact():
  global next_id
  contact = {
    "id" : next_id,
    "name" : validator.validate_name(),
    "number" : validator.validate_number(),
    "email" : validator.validate_email()
  }
  contacts.append(contact)
  next_id += 1

def update_contact():
  id = validator.validate_id()
  found = False
  for contact in contacts:
    if contact["id"] == id:
      contact["name"] = validator.validate_name()
      contact["number"] = validator.validate_number()
      contact["email"] = validator.validate_email()
      print(f"{id} updated successfully.")
      found = True
      break
  if not found:
    print("ID not found.")
