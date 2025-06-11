def validate_name():
  while True:
    name = input("Enter name:")
    if name.isalpha():
      return name
    else:
     print("Name can only contain letters.")
    
def validate_number():
  while True:
      number = input("Enter number: ")
      if len(number) != 11:
          print("Number must be 11 digits long.")
          continue
      if not number.isdigit():
          print("Number can only contain digits.")
          continue
      return number

def validate_email():
  while True:
    email = input("Enter email:")
    if "@" in email and (email.endswith(".com") or email.endswith(".co.uk")):
      return email
    else:
      print("Email must contain @ and end in .com or .co.uk")

def validate_id():
  while True:
    id = input("Enter ID:")
    if id.isdigit():
      return int(id)
    else:
      print("ID must be a number.")