# This script was originally based off Dr Angela Lu's Udemy Python course project
# I've expanded the scope to enforce some restrictions - minimum length, at least 1 of every character etc.
# Future - have the program properly loop back to the start if a valid password is not generated.
import random
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def is_valid_value(user_input):
    try:
        return_value = int(user_input)
        return True, return_value
    except TypeError, ValueError:
        print("Non-integer detected, re-enter selection.")
        return False, 0

print("Welcome to the PyPassword Generator!")
valid_letters = valid_numbers = valid_symbols = False

while not valid_letters or not valid_numbers or not valid_symbols:
    nr_letters = input("How many letters would you like in your password?\n"
                       "(A random amount of them will be selected as UPPER CASE)\n")
    nr_symbols = input(f"How many symbols would you like?\n")
    nr_numbers = input(f"How many numbers would you like?\n")
    valid_letters, nr_letters = is_valid_value(nr_letters)
    valid_symbols, nr_symbols= is_valid_value(nr_symbols)
    valid_numbers, nr_numbers = is_valid_value(nr_numbers)

if nr_letters == 0 or nr_symbols == 0 or nr_numbers == 0:
    print("You must choose at least one of each character type to generate a strong password.")
else:
    if nr_letters + nr_symbols + nr_numbers < 10:
        print("Minimum password length is 10 characters.")
    else:
        password = []
        #Generate at least 1 upper case character for every password
        number_of_upper = random.randint(1,nr_letters)
        number_of_lower = nr_letters - number_of_upper
        print(f"Generating a password with {number_of_lower} lower case and {number_of_upper} upper case letters, {nr_numbers} numbers and {nr_symbols} special characters.")
        if number_of_lower > 0:
            # Conceivably we could end up with a password with no lower case characters
            for letter in range(0, number_of_lower):
                password.append(random.choice(lower_letters))
        for letter in range(0, number_of_upper):
            password.append(random.choice(upper_letters))
        for symbol in range(0, nr_symbols):
            password.append(random.choice(symbols))
        for number in range (0, nr_numbers):
            password.append(random.choice(numbers))
        random.shuffle(password)
        final_password = "".join(password)
        print(final_password)
