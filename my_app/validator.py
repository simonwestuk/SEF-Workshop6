def validate_id():
  while True:
      contact_id = input("Enter ID: ")
      if contact_id.isdigit():
          return int(contact_id)
      else:
          print("ID must be a number.")

def validate_name():
  while True:
      name = input("Enter name: ")
      if all(part.isalpha() for part in name.split()):
          return name
      else:
          print("Name can only contain letters and spaces.")

def validate_number():
  while True:
      number = input("Enter number: ")
      if len(number) != 11 or not number.isdigit():
          print("Number must be 11 digits and contain only digits.")
      else:
          return number

def validate_email():
  while True:
      email = input("Enter email: ")
      if "@" in email and (email.endswith(".com") or email.endswith(".co.uk")):
          return email
      else:
          print("Email must contain '@' and end in .com or .co.uk")

def validate_address():
  while True:
      address = input("Enter address: ")
      if len(address.strip()) > 5:
          return address
      else:
          print("Address must be more descriptive.")

def validate_date_of_birth():
  while True:
      dob = input("Enter date of birth (YYYY-MM-DD): ")
      try:
          year, month, day = map(int, dob.split("-"))
          import datetime
          datetime.date(year, month, day)  # check validity
          return dob
      except (ValueError, TypeError):
          print("Date must be in format YYYY-MM-DD and be valid.")

def validate_company():
  while True:
      company = input("Enter company name: ")
      if company.strip():
          return company
      else:
          print("Company name cannot be empty.")

def validate_notes():
  notes = input("Enter notes (optional): ")
  return notes.strip()
