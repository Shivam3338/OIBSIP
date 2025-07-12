import random
import string

def get_length():
    """
    Gets password length from user.
    Returns:
        int: The password length.
    """
    while True:
        try:
            length = int(input("Enter password length (e.g., 12): "))
            if length <= 0:
                print("Length must be positive. Try again.")
            else:
                return length
        except ValueError:
            print("Bad input. Enter a number for length.")

def get_types():
    """
    Gets character types from user.
    Returns:
        tuple: Booleans for letters, numbers, symbols.
    """
    while True:
        include_letters_input = input("Include letters (y/n)? ").lower()
        include_numbers_input = input("Include numbers (y/n)? ").lower()
        include_symbols_input = input("Include symbols (y/n)? ").lower()

        include_letters = include_letters_input == 'y'
        include_numbers = include_numbers_input == 'y'
        include_symbols = include_symbols_input == 'y'

        if not (include_letters or include_numbers or include_symbols):
            print("Pick at least one type. Try again.")
        else:
            return include_letters, include_numbers, include_symbols

def make_password(length, include_letters, include_numbers, include_symbols):
    """
    Makes a random password.
    Args:
        length (int): Password length.
        include_letters (bool): Include letters.
        include_numbers (bool): Include numbers.
        include_symbols (bool): Include symbols.
    Returns:
        str: The new password.
    """
    chars = ""
    if include_letters:
        chars += string.ascii_letters
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    if not chars:
        return "Error: No types picked."

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    """
    Runs the password maker.
    """
    print("--- Password Maker ---")

    password_length = get_length()
    include_letters, include_numbers, include_symbols = get_types()

    made_password = make_password(
        password_length,
        include_letters,
        include_numbers,
        include_symbols
    )

    print(f"\nYour Password: {made_password}")
    print("----------------------")

if __name__ == "__main__":
    main()