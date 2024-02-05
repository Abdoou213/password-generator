import random
import string

def generate_password():
    # Prompt the user for a password length between 15 and 30 characters
    while True:
        try:
            length = int(input("Enter the password length (between 15 and 30): "))
            if 15 <= length <= 30:
                break
            else:
                print("Invalid input. Password length must be between 15 and 30.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Ensure the length is within the specified range of 15 to 30 characters
    length = max(15, min(30, length))

    chars = string.ascii_letters
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    # Initially, generate the password with the required length minus the number of conditions to ensure inclusion
    conditions_count = use_digits + use_special_chars
    base_length = max(0, length - conditions_count)
    password = ''.join(random.choice(chars) for _ in range(base_length))

    # Ensure at least one digit and one special character are included if required
    if use_digits:
        password += random.choice(string.digits)
    if use_special_chars:
        password += random.choice(string.punctuation)

    # Shuffle the password to avoid predictability of the last characters being digits/special
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    print("Generated Password:", password)

def main():
    # Call the function to generate and print the password
    generate_password()

if __name__ == "__main__":
    main()
