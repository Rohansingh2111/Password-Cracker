# encryption.py

from cryptography.fernet import Fernet

def encrypt_message(key, message):
    """Encrypt a message using the provided key."""
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(message.encode())
    return cipher_text

def decrypt_message(key, cipher_text):
    """Decrypt a message using the provided key."""
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(cipher_text)
    return decrypted_text.decode()
