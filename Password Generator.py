import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    if not (use_uppercase or use_lowercase or use_digits or use_special):
        raise ValueError("At least one character type must be selected")

    char_pool = ''
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1")

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator Tool")
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please enter a valid number for the length.")
        return

    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    use_special = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
