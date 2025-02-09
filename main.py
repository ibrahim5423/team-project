import random
import string

def generate_password(length=12):
    """Generate a strong random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate and print a random password of length 12
print("Generated Password:", generate_password())
