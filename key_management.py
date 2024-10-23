# key_management.py

from cryptography.fernet import Fernet

def generate_key():
    """Generate a new encryption key."""
    return Fernet.generate_key()

def save_key(key, filename='secret.key'):
    """Save the encryption key to a file."""
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename='secret.key'):
    """Load the encryption key from a file."""
    with open(filename, 'rb') as key_file:
        return key_file.read()
