"""
Task 4: Password Generator (CLI)
Synent Technologies - Python Development Internship
Author: Your Name
"""

import secrets
import string
import datetime
import os


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generate a secure password based on user preferences."""
    charset = ""

    if use_upper:
        charset += string.ascii_uppercase
    if use_lower:
        charset += string.ascii_lowercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation

    if not charset:
        print("❌ Error: At least one character type must be selected!")
        return None

    # Ensure at least one character from each selected type
    password = []
    if use_upper:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    # Fill the rest randomly
    while len(password) < length:
        password.append(secrets.choice(charset))

    # Shuffle to avoid predictable pattern
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def check_strength(password):
    """Check and return password strength."""
    score = 0
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1
    if len(password) >= 16:
        score += 1

    if score <= 2:
        return "🔴 Weak"
    elif score == 3:
        return "🟡 Medium"
    elif score == 4:
        return "🟢 Strong"
    else:
        return "🔵 Very Strong"


def save_password(password, strength):
    """Save password to a log file with timestamp."""
    filename = "password_log.txt"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] Password: {password} | Strength: {strength}\n")
    print(f"✅ Password saved to '{filename}'")


def get_yes_no(prompt):
    """Helper to get yes/no input."""
    while True:
        choice = input(prompt + " (y/n): ").strip().lower()
        if choice in ("y", "n"):
            return choice == "y"
        print("   Please enter 'y' or 'n'.")


def main():
    print("=" * 50)
    print("   🔐 Secure Password Generator")
    print("   Synent Technologies Internship")
    print("=" * 50)

    while True:
        print("\n--- Settings ---")

        # Get password length
        while True:
            try:
                length = int(input("Enter password length (8-64): "))
                if 8 <= length <= 64:
                    break
                print("   Length must be between 8 and 64.")
            except ValueError:
                print("   Please enter a valid number.")

        # Get character preferences
        use_upper   = get_yes_no("Include Uppercase letters? (A-Z)")
        use_lower   = get_yes_no("Include Lowercase letters? (a-z)")
        use_digits  = get_yes_no("Include Numbers?          (0-9)")
        use_symbols = get_yes_no("Include Special Symbols?  (!@#...)")

        # Generate password
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

        if password:
            strength = check_strength(password)
            print("\n" + "=" * 50)
            print(f"  Generated Password : {password}")
            print(f"  Strength           : {strength}")
            print("=" * 50)

            # Ask to save
            if get_yes_no("\nSave this password to log file?"):
                save_password(password, strength)

        # Ask to generate another
        if not get_yes_no("\nGenerate another password?"):
            print("\n👋 Thank you for using Password Generator!")
            print("   - Synent Technologies Internship\n")
            break


if __name__ == "__main__":
    main()
