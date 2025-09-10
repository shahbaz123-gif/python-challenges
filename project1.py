import random
import string

def generate_password(length=12):
    """
    Generate a strong random password with uppercase, lowercase letters, and numbers
    
    Args:
        length (int): Length of the password (default: 12)
    
    Returns:
        str: Generated password
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    
    # Combine all character sets
    all_characters = lowercase + uppercase + digits
    
    # Ensure at least one character from each category
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    
    # Fill the remaining length with random characters from all sets
    remaining_length = length - len(password_chars)
    password_chars.extend(random.choice(all_characters) for _ in range(remaining_length))
    
    # Shuffle the password to make it more random
    random.shuffle(password_chars)
    
    # Convert list to string
    password = ''.join(password_chars)
    
    return password

def generate_multiple_passwords(num_passwords=5, length=12):
    """
    Generate multiple random passwords
    
    Args:
        num_passwords (int): Number of passwords to generate
        length (int): Length of each password
    
    Returns:
        list: List of generated passwords
    """
    passwords = []
    for i in range(num_passwords):
        password = generate_password(length)
        passwords.append(password)
    return passwords

def main():
    """Main function to demonstrate password generation"""
    print("🔐 Random Password Generator 🔐")
    print("=" * 40)
    
    try:
        # Get user input
        length = int(input("Enter password length (minimum 8): ") or "12")
        if length < 8:
            print("Password length too short! Using minimum length of 8.")
            length = 8
        
        num_passwords = int(input("How many passwords to generate? (default: 1): ") or "1")
        
        if num_passwords == 1:
            # Generate single password
            password = generate_password(length)
            print(f"\n✅ Your generated password:")
            print(f"🔒 {password}")
            print(f"📏 Length: {len(password)} characters")
        else:
            # Generate multiple passwords
            passwords = generate_multiple_passwords(num_passwords, length)
            print(f"\n✅ Generated {num_passwords} passwords:")
            for i, password in enumerate(passwords, 1):
                print(f"{i:2d}. {password} (length: {len(password)})")
        
        # Show password strength info
        print(f"\n💪 Password contains: lowercase, uppercase letters, and numbers")
        
    except ValueError:
        print("❌ Please enter valid numbers!")

# Additional utility function
def check_password_strength(password):
    """
    Check the strength of a password
    
    Args:
        password (str): Password to check
    
    Returns:
        str: Strength assessment
    """
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    if len(password) >= 12 and has_lower and has_upper and has_digit:
        return "Strong"
    elif len(password) >= 8 and has_lower and has_upper and has_digit:
        return "Medium"
    else:
        return "Weak"

if __name__ == "__main__":
    # Run the main program
    main()
    
    # Example usage of the functions
    print("\n" + "=" * 40)
    print("🎲 Example generated passwords:")
    print("=" * 40)
    
    # Generate some example passwords
    examples = generate_multiple_passwords(3, 16)
    for i, pwd in enumerate(examples, 1):
        strength = check_password_strength(pwd)
        print(f"Example {i}: {pwd} - {strength}")