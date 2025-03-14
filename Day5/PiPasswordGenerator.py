#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# letter_selected = ''
# symbol_selected = ''
# numbers_selected = ''
# i = 0
# while i < nr_letters:
#  letter_selected += random.choice(letters)
#  i = i + 1 

# i = 0
# while i < nr_symbols:
#   symbol_selected += random.choice(symbols)
#   i = i + 1 

# i = 0
# while i < nr_numbers:
#  numbers_selected += random.choice(numbers)
#  i = i + 1 
# print (letter_selected + symbol_selected + numbers_selected)
# -----------------Alternative Solution--------
# password = ''

# for char in range(0, nr_letters):
#     password += random.choice(letters)
# for char in range(0, nr_symbols):
#     password += random.choice(letters)
# for char in range(0, nr_numbers):
#     password += random.choice(letters)
# print (password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#for this we need to convert to a list
password_list = [] 
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list) #this shuffles the list of characters in the password

password = '' # created a new password variable to hold the new 

for char in password_list: #for each character in the password_list add the character to the password variable
    password += char

print (f"Your password is: {password}")