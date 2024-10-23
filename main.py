# main.py

from key_management import generate_key, save_key, load_key
from encryption import encrypt_message, decrypt_message

def main():
    # Generate and save a new key
    key = generate_key()
    save_key(key)
    print(f"Key generated and saved to 'secret.key': {key.decode()}")

    # Load the key for encryption/decryption
    key = load_key()
    
    # Input message from the user
    plain_text = input("Enter a message to encrypt: ")
    
    # Encrypt the message
    cipher_text = encrypt_message(key, plain_text)
    print(f"Cipher Text: {cipher_text.decode()}")

    # Decrypt the message
    decrypted_text = decrypt_message(key, cipher_text)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
