import random
import string

def generate_password(length=12):
    """
    Generate a random password with given length
    Default length is 12 characters
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    
    # Combine all characters
    all_characters = lowercase + uppercase + digits
    
    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    
    # Fill the rest with random characters from all categories
    for _ in range(length - 3):
        password.append(random.choice(all_characters))
    
    # Shuffle the password to make it more random
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

# Generate and print passwords
print("Basic Password Generator:")
print("-" * 30)
for i in range(5):
    password = generate_password()
    print(f"Password {i+1}: {password}")