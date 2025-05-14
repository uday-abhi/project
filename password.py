import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    characters = string.ascii_letters  # A-Z and a-z

    if use_digits:
        characters += string.digits  # 0-9
    if use_special:
        characters += string.punctuation  # !@#$%^&*() etc.

    if length < 4:
        return "Password too short! Use at least 4 characters."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main Program
print("🔐 Password Generator")
length = int(input("Enter desired password length: "))
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

generated_password = generate_password(length, use_digits, use_special)
print("\nGenerated Password:", generated_password)
