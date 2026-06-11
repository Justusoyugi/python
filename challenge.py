import random
import os
os.system('cls' if os.name == 'nt' else 'clear')

# Print fn
print("""Your learning path:
      \t-Python basics
      \t-Data engeneering
      \t-AI""")

# Variable fn
email = "justusoyugi02.com"  # Hardcoded variable
print("info @", email)
print("support @", email)
print("www.", email)

# Input fn
# name = input( "Name:") #Dynamic variable because it is user dictated
# print ("Your name is", name)

# Data types
# a = 10 #integer
# b = 3.142 # float
# c = "Hello" # string
# d = "1234" # string
# e = True # bool
# f = False # bool
# g = None #none type
# h = " " #str empty space

# Data type Challenge
a = 24
b = 6.1
c = "Justus Oyugi"
d = True
e = None

print(a)
print(b)
print(c)
print(d)
print(e)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(c.upper())
print(a.bit_length())
print(len(c))

# Working with strings

Phone = "+49 (176) 123-4567"
print(Phone.replace("+", "00").replace("-", "").replace(" ",
      "").replace("(", "").replace(")", " "))

Details = "968-Maria,( D@t@ Engineer ) ;; 27 y  "
name = Details[4:9].lower()
print(f"name:  {name}")
role = Details[11:26].replace("@", "a").lower().strip()
print(f"role: {role}")
age = Details[-6:-4]
print(f"age: {age}")

# Working with number

x = random.randint(1, 100)
print(x)
x %= 2
print(x)
if x == 0:
    print("Even number")

else:
    print("Odd number")

# Check if a user's name is not empty and the age is greater than or equal to 18.
# username = ""
# age = 20
# print(username )

# Check if the password is atleast 8 characters long and does not contain spaces.


# Check if a user's email is not empty, contains '@', and ends with '.com'.


# Check if a username is a string, is not None, and is longer tahn 5 characters.


# Check if the user is either an admin or a moderator, and either they are not banned or they've verified their email.


# validate the quality and correctness of the email values.


email = "diego@g.com"

# Clean the str
email = email.strip()
valid = True
# Must not be empty
if email == "":
    print("Email must not be empty")
    valid = False
# Must contain '.' and '@'
if not ("." in email and "@" in email):
    print("Email must contain '.' and '@'")
    valid = False
# Must contain exactly one @ symbol
if email.count("@") != 1:
    print("Email must  contain exactly one '@' symbol")
    valid = False
# Must end with '.com' , '.org' , or '.net'
if not (email.endswith((".com", ".org", ".net"))):
    print("Email must end with '.com','.org','.net'")
    valid = False
# Must not be longer than 20 characters
if len(email) > 20:
    print("Email must not be longer than 20 characters")
    valid = False
# Must start and end with a letter or digit
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
    valid = False
if valid:
    print("Email is valid")
    # To check all the issues in the emai we use independent if.

    # Validate the quality and correctness of passwords.

    # 4.Must include atleast 1 lowercase

    password = "dego@g.com"
    # Clean str
    password = password.strip()

 # 1.Must not be empty
if password == "":
    print("Password must not be empty")
# 2.Must be atleast 8 characters
elif not len(password) >= 8:
    print("Password must be atleast 8 characters")
 # 3.Must include atleast 1 uppercase
# for char in password:
 #   if char.isupper():
  #      print("Password must include atleast 1 uppercase")

# 5.Must not be same as email
elif password == email:
    print("Password must not be same as email")
# 6.Must not contain any spaces
# elif not password != password.strip():
 #   print("Password must not contain any apace")

 # 7.Must start and end with a letter or a digit
elif not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or a digit")
else:
    print("Password is valid")

    # LOOPS

    # For Loop

items = (1, 2, 3, 4, 5)
for item in items:
    print(f"Round : {item}")
# another way is to use range, firstitem will show but the last won't.
for item in range(1, 6):
    print(f"Round : {item}")

# Example
files = [' Report.csv ', 'DATA.csv ', ' final.TXT']
for file in files:
    file = file.strip().lower().replace('txt', 'csv')
    print(f"processing {file}")

# Print the 7 times table from 1 to 10 using for loop
for item in range(1, 11):
    answer = 7 * item
    print(f"7 * {item} = {answer}")

    # print a left aligned star with 6 rows
for x in range(1, 7):
    print("*" * x)

    # For loop, if , (break, continue, pass), else(only after break)

    # Check if any filename appear more than once. Print 'Duplicate found' if a duplicate exists, otherwise print ' All files are unique'.

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
duplicate = False
# seen = set()

for file in file_list:
    if file in file_list:  # seen:
        duplicate = True
        # print(f"Duplicate found: {file}")
        break
    file_list.add(file)
print("Duplicates found:", duplicate)

# While loop

# While condition loop
# answer = ""
# while answer != "yes":
#    answer = input("Do you agree?(yes/no):")
# print("Thank you")

# While True
# while True:
#    answer = input("Do you agree?(yes/no):")
#    if answer == "yes":
#        break
# print("Thank you")

# Allow up to 3 attempts
# If the user types "yes" print "Glad we're on the same page"
# Otherwise print 3 strikes you are out.

# attempts = 0
# while attempts < 3:
#    answer = input("Do you agree?(yes/no):")
#    if answer == "yes":
#        print("Glad we're on the same page")
# break
#    attempts += 1
# else:
#    print("3 strikes, you're out")

# For loop exercise
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
